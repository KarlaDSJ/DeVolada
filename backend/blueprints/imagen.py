from main import db
from flask import app
from flask import Blueprint, request, jsonify
from models.imagenM import Imagen
from models.productoM import Producto
from schemas.imagenE import ImagenEsquema
from werkzeug.utils import secure_filename
from PIL import Image
import os
import base64
import io

imagen = Blueprint('imagen', __name__)

imagen_esquema = ImagenEsquema()
imagenes_esquema = ImagenEsquema(many=True)

# Límite de imagenes que se pueden subir por producto
IMG_LIMIT = 5

# Dirección de la carpeta donde se guardarán los archivos de las imágenes
SAVE_PATH = os.path.join("static", "ImagenesProductos")


# Petición para agregar una lista de imagenes a la base de datos y guardarlas en el sistema.
# Las imagenes deben de pasarse en formato base64
@imagen.route('/imagenes/subir/<idProducto>', methods = ['POST'])
def sube_imagenes(idProducto):
    # Verifica que el producto exista
    producto = db.session.query(Producto).filter_by(idProducto=idProducto).first()
    if (producto is None):
        return jsonify({"error": 101, 
                        "mensaje": "No se pudo subir la imagen. El producto <" + str(idProducto) + "> no existe."})

    # Cuenta las imagenes que tiene el producto
    cantidad_imgs_producto = db.session.query(Imagen).filter_by(idProducto=idProducto).count()

    # Cuenta las imagenes que se van a subir
    cantidad_imgs_subir = len(request.json)

    # Verifica que no se exceda la cantidad de imagenes permitidas
    if( cantidad_imgs_producto + cantidad_imgs_subir > IMG_LIMIT ):
        return jsonify({"error": 102,
                        "mensaje": "No se pudieron subir las imagenes. Se ha excedido el límite de imagenes (" 
                        + str(cantidad_imgs_producto + cantidad_imgs_subir) + ") para el producto <" + str(idProducto) + ">"})

    # Sube y guarda las imagenes
    for i in range(cantidad_imgs_subir):
        # Datos de la imagen codificados en base64
        imagen_bin = request.json[i] 
        # Elimina el header de los datos URI
        imagen_bin = imagen_bin[imagen_bin.find(",")+1:]
        # Nombre que tendrá la img
        imagen_nombre  = "product" + idProducto + "_img" + str(cantidad_imgs_producto + i + 1)
        # Ruta donde se guardará la img
        imagen_ruta = os.path.join(SAVE_PATH, secure_filename(imagen_nombre))

        # Guarda la imagen en el sistema
        with open(imagen_ruta, "wb") as fh:
            fh.write(base64.b64decode(imagen_bin))

        # Agrega la direccion de la imagen a la BD
        imagen_nueva = Imagen(imagen_ruta, idProducto)
        db.session.add(imagen_nueva) # Guarda la entrada en la BD

    # Guarda los cambios en la BD
    db.session.commit()

    return jsonify({"mensaje": "Se subieron las imagenes del producto <" + str(idProducto) + "> correctamente." })

# Petición para actualizar las imagenes de un producto, reemplando las anteriores.
# Borra todas las imagenes anteriores de la base de datos y del sistema, 
# despues agrega las nuevas imagenes a la base de datos y las guarda en el sistema.
# Las imagenes deben de pasarse en formato base64
@imagen.route('/imagenes/actualiza/<idProducto>', methods = ['PATCH'])
def actualiza_imagenes(idProducto):

    # Verifica que el producto exista
    producto = db.session.query(Producto).filter_by(idProducto=idProducto).first()
    if (producto is None):
        return jsonify({"error": 101, 
                        "mensaje": "No se pudieron borrar las imagenes. " + 
                        "El producto <" + str(idProducto) + "> no existe."})

    # Busca las imagenes existentes en el producto
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

    # Cuenta las imagenes que se van a subir
    cantidad_imgs_subir = len(request.json)

    # Verifica que no se exceda la cantidad de imagenes permitidas
    if( cantidad_imgs_subir > IMG_LIMIT ):
        return jsonify({"error": 102,
                        "mensaje": "No se pudieron subir las imagenes. Se ha excedido el límite de imagenes (" 
                        + str(cantidad_imgs_subir) + ") para el producto <" + str(idProducto) + ">"})

    # Sube y guarda las nuevas imágenes
    for i in range(cantidad_imgs_subir):
        # Datos de la imagen codificados en base64
        imagen_bin = request.json[i] 
        # Elimina el header de los datos URI
        imagen_bin = imagen_bin[imagen_bin.find(",")+1:]
        # Nombre que tendrá la img
        imagen_nombre  = "product" + idProducto + "_img" + str( i + 1)
        # Ruta donde se guardará la img
        imagen_ruta = os.path.join(SAVE_PATH, secure_filename(imagen_nombre))

        # Guarda la imagen en el sistema
        with open(imagen_ruta, "wb") as fh:
            fh.write(base64.b64decode(imagen_bin))

        # Agrega la direccion de la imagen a la BD
        imagen_nueva = Imagen(imagen_ruta, idProducto)
        db.session.add(imagen_nueva) # Guarda la entrada en la BD

    # Guarda los cambios en la BD
    db.session.commit()

    return jsonify({"mensaje": "Se actualizaron las imagenes del producto <" + str(idProducto) + "> correctamente." })

# Petición para consultar la direccion de una imagen desde la base de datos a través de su PK. 
@imagen.route('/imagen', methods=['GET'])
def obten_imagen():
    imagen = request.json['imagen']
    idProducto = request.json['idProducto']
    imagen_obtenida = db.session.query(Imagen).get((imagen,idProducto))
    return jsonify({"imagen:": imagen_obtenida.imagen})


# Petición para obtener las imagenes en base64 de un producto. 
@imagen.route('/imagenes/producto/<idProducto>', methods=['GET'])
def obten_imagenes64_producto(idProducto):

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

        # Obtiene la dirección del archivo de la imagen
        imgPath = img["imagen"]
        
        # Verifica que exista el archivo de la imagen en la dirección dada
        if not os.path.exists(imgPath):
            return jsonify({"error": 101, "mensaje": "No se encontró la imagen con ruta <" + imgPath + ">."})
        
        # Decodifica la imagen en base64
        with open(imgPath,"rb") as img_file:
            ext = "jpeg" #imgPath.split('.')[-1]
            prefix = f'data:image/{ext};base64,'
            imagen_decodificada = prefix + base64.b64encode(img_file.read()).decode('utf-8')
            imagenes_data.append( imagen_decodificada )

    return jsonify(imagenes_data)


# Petición para obtener la primer imagen en base64 de un producto. 
@imagen.route('/imagen/producto/<idProducto>', methods=['GET'])
def obten_imagen64_producto(idProducto):

    # Verifica que el producto exista
    producto = db.session.query(Producto).filter_by(idProducto=idProducto).first()
    if (producto is None):
        return jsonify({"error": 101, 
                        "mensaje": "No se pudieron obtener las imagenes. " + 
                        "El producto <" + str(idProducto) + "> no existe."})

    # Obtiene las rutas de las imagenes desde la BD
    imagen_producto = db.session.query(Imagen).filter_by(idProducto=idProducto).first()
    imagen_url =  imagen_esquema.dump(imagen_producto)
    imagen_data = []

    # Obtiene la dirección del archivo de la imagen
    imgPath = imagen_url["imagen"]
        
    # Verifica que exista el archivo de la imagen en la dirección dada
    if not os.path.exists(imgPath):
        return jsonify({"error": 101, "mensaje": "No se encontró la imagen con ruta <" + imgPath + ">."})
        
    # Decodifica la imagen en base64
    with open(imgPath,"rb") as img_file:
        ext = "jpeg" #imgPath.split('.')[-1]
        prefix = f'data:image/{ext};base64,'
        imagen_decodificada = prefix + base64.b64encode(img_file.read()).decode('utf-8')
        imagen_data.append( imagen_decodificada )

    return jsonify(imagen_data)


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