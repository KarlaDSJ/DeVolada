from main import db
from flask import app
from flask import Blueprint, request, jsonify
from models.imagenM import Imagen
from models.productoM import Producto
from schemas.imagenE import ImagenEsquema
from werkzeug.utils import secure_filename
import os
import base64

imagen = Blueprint('imagen', __name__)

imagen_esquema = ImagenEsquema()
imagenes_esquema = ImagenEsquema(many=True)

# Límite de imagenes que se pueden subir por producto
IMG_LIMIT = 5

# Dirección de la carpeta donde se guardarán los archivos de las imágenes
SAVE_PATH = os.path.join("static", "ImagenesProductos")


# Petición para agregar una lista de imagenes a la base de datos y guardarlas en el sistema.
# Deben de pasarse a través de un formData
@imagen.route('/imagenes/subir/<idProducto>', methods = ['POST'])
def subir_imagenes(idProducto):

    # Verifica que el producto exista
    producto = db.session.query(Producto).filter_by(idProducto=idProducto).first()
    if (producto is None):
        return jsonify({"error": 101, 
                        "mensaje": "No se pudo subir la imagen. El producto <" + str(idProducto) + "> no existe."})

    # Cuenta las imagenes que tiene el producto
    cantidad_imgs_producto = db.session.query(Imagen).filter_by(idProducto=idProducto).count()

    # Cuenta las imagenes que se van a subir
    cantidad_imgs_subir = len(request.files)

    # Verifica que no se exceda la cantidad de imagenes permitidas
    if( cantidad_imgs_producto + cantidad_imgs_subir > IMG_LIMIT ):
        return jsonify({"error": 102,
                        "mensaje": "No se pudieron subir las imagenes. Se ha excedido el límite de imagenes (" 
                        + str(cantidad_imgs_producto + cantidad_imgs_subir) + ") para el producto <" + str(idProducto) + ">"})


    for i in range(cantidad_imgs_subir):

        # Obtiene los datos de la imagen 
        imagen_data = request.files["imagen["+str(i)+"]"]

        # Crea el nombre que tendrá la img
        imagen_nombre  = "product" + idProducto + "_img" + str(cantidad_imgs_producto + i + 1)

        # Crea la ruta donde se guardará la img
        imagen_url = os.path.join(SAVE_PATH, secure_filename(imagen_nombre))

        # Agrega a la BD la direccion donde se guardará la imagen y guarda la imagen
        imagen_nueva = Imagen(imagen_url, idProducto)
        db.session.add(imagen_nueva) # Guarda la entrada en la BD
        imagen_data.save(imagen_url) # Guarda la imagen en el sistema

    # Guarda los cambios en la BD
    db.session.commit()

    return jsonify({"mensaje": "Se subieron las imagenes correctamente al producto <" + str(idProducto) + ">" })


# Petición para eliminar una imagen de la base de datos a través de su PK. 
@imagen.route('/imagen', methods=['DELETE'])
def elimina_imagen():
    imagen = request.json['imagen']
    idProducto = request.json['idProducto']
    imagen_eliminada = db.session.query(Imagen).get((imagen,idProducto))
    num_imagenes_producto = db.session.query(Imagen).filter_by(idProducto=idProducto).count()
    if ( num_imagenes_producto > 1 ):
        db.session.delete(imagen_eliminada)
        db.session.commit()
        return jsonify({"mensaje:": "Se eliminó la imagen correctamente"})
    return jsonify({"mensaje:": " No se puede eliminar la unica imagen del producto"})


# Petición para consultar una imagen de la base de datos a través de su PK. 
@imagen.route('/imagen', methods=['GET'])
def obten_imagen():
    imagen = request.json['imagen']
    idProducto = request.json['idProducto']
    imagen_obtenida = db.session.query(Imagen).get((imagen,idProducto))
    return jsonify({"imagen:": imagen_obtenida.imagen})


# Petición para consultar todas las imagenes de un producto. 
@imagen.route('/imagenes/producto/<idProducto>', methods=['GET'])
def obten_imagenes_producto(idProducto):

    # Verifica que el producto exista
    producto = db.session.query(Producto).filter_by(idProducto=idProducto).first()
    if (producto is None):
        return jsonify({"error": 101, 
                        "mensaje": "No se pudieron obtener las imagenes. " + 
                        "El producto <" + str(idProducto) + "> no existe."})

    # Obtiene las rutas de las imagenes desde la BD
    imagenes_producto = db.session.query(Imagen).filter_by(idProducto=idProducto).all()
    imagenes_url =  imagenes_esquema.dump(imagenes_producto)
    imagenes_data = []

    for img in imagenes_url:

        # Obtiene la dirección de la imagen
        imgPath = img["imagen"]
        print("IMG: " + imgPath)
        
        # Verifica que exista el archivo de la imagen en la dirección dada
        if not os.path.exists(imgPath):
            return jsonify({"error": 101, "mensaje": "No se encontró la imagen con ruta <" + imgPath + ">."})
        
        # Obtiene la imagen decodificada
        with open(imgPath,"rb") as img_file:
            imagen_decodificada = base64.b64encode(img_file.read()).decode('utf-8')
            imagen_data = {"file": imagen_decodificada, "img": "" }
            imagenes_data.append( imagen_data )

    return jsonify(imagenes_data)


# Petición para eliminar todas las imagenes de un producto ( DB y archivos). 
@imagen.route('/imagenes/producto/<idProducto>', methods=['DELETE'])
def elimina_imagenes_producto(idProducto):

    # Verifica que el producto exista
    producto = db.session.query(Producto).filter_by(idProducto=idProducto).first()
    if (producto is None):
        return jsonify({"error": 101, 
                        "mensaje": "No se pudieron borrar las imagenes. " + 
                        "El producto <" + str(idProducto) + "> no existe."})

    # Borra las imagenes existentes en el producto
    imagenes_producto = db.session.query(Imagen).filter_by(idProducto=idProducto).all()
    imagenes_cantidad = len(imagenes_producto)

    # Elimina las entradas de las imagenes en la BD
    for img in imagenes_producto:
        db.session.delete(img) # Elimina la entrada en la BD
    db.session.commit()

    # Elimina los archivos de las imagenes de la carpeta static
    imagenes_producto = imagenes_esquema.dump(imagenes_producto)
    for img in imagenes_producto:
        imgPath = img["imagen"]
        if os.path.exists(imgPath):
            os.remove(imgPath) # Elimina el archivo en el sistema
        else:
            print("No se pudo borrar el archivo de imagen <" + imgPath + "> porque no existe.")

    return jsonify({"mensaje:": "Se eliminaron " + str(imagenes_cantidad) 
        + " imagenes del producto <" + str(idProducto) + "> correctamente."})