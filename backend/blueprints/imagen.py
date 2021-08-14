from main import db
from flask import app
from flask import Blueprint, request, jsonify
from models.imagenM import Imagen
from models.productoM import Producto
from schemas.imagenE import ImagenEsquema
from werkzeug.utils import secure_filename
import os
import base64
import pprint

imagen = Blueprint('imagen', __name__)

imagen_esquema = ImagenEsquema()
imagen_esquema = ImagenEsquema(many=True)

# Límite de imagenes que se pueden subir por producto
IMG_LIMIT = 5

# Petición para agregar una imagen a la base de datos y guardarla en el sistema.
@imagen.route('/imagen/subir/<idProducto>', methods = ['POST'])
def subir_imagen(idProducto):

    # Verifica que el producto exista
    producto = db.session.query(Producto).filter_by(idProducto=idProducto).first()
    if (producto is None):
        return jsonify({"error": 101, 
                        "mensaje": "No se pudo subir la imagen. El producto <" + str(idProducto) + "> no existe."})

    # Cuenta las imagenes que tiene el producto
    cantidad_imgs = db.session.query(Imagen).filter_by(idProducto=idProducto).count()

    # Verifica que no se exceda la cantidad de imagenes permitidas
    if( cantidad_imgs >= IMG_LIMIT ):
        return jsonify({"error": 102,
                        "mensaje": "No se pudo subir la imagen. Se ha excedido el límite de imagenes (" 
                        + str(cantidad_imgs) + ") para el producto <" + str(idProducto) + ">"})

    # Obtiene los datos de la imagen 
    imagen_data    = request.files['imagen']

    # Crea el nombre que tendrá la img
    imagen_nombre  = "product" + idProducto + "_img" + str(cantidad_imgs + 1)

    # Crea la ruta donde se guardará la img
    imagen_url = os.path.join("static", "ImagenesProductos", secure_filename(imagen_nombre))

    # Agrega a la BD la direccion donde se guardará la imagen y guarda la imagen
    imagen_nueva = Imagen(imagen_url, idProducto)
    db.session.add(imagen_nueva) # Guarda la entrada a la BD
    imagen_data.save(imagen_url) # Guarda la imagen en el sistema

    # Guarda los cambios en la BD
    db.session.commit()

    return jsonify({"mensaje": "Se subió la imagen correctamente", 
                    "url": imagen_url })

# Petición para agregar imagenes a la base de datos y guardarlas en el sistema.
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
        imagen_url = os.path.join("static", "ImagenesProductos", secure_filename(imagen_nombre))

        # Agrega a la BD la direccion donde se guardará la imagen y guarda la imagen
        imagen_nueva = Imagen(imagen_url, idProducto)
        db.session.add(imagen_nueva) # Guarda la entrada a la BD
        imagen_data.save(imagen_url) # Guarda la imagen en el sistema

    # Guarda los cambios en la BD
    db.session.commit()

    return jsonify({"mensaje": "Se subió la imagen correctamente", 
                    "url": imagen_url })




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
@imagen.route('/imagen/producto/<id>', methods=['GET'])
def obten_imagenes_producto(id):
    producto = id
    imagenes_producto_url = db.session.query(Imagen).filter_by(idProducto=producto).all()
    imagenes_url =  imagen_esquema.dump(imagenes_producto_url)
    print(imagenes_producto_url)
    imagenes_data = []

    for img_url in imagenes_url:
        url_imagen = img_url["imagen"]
        with open(url_imagen,"rb") as img_file:
            imagenes_data.append( base64.b64encode(img_file.read()).decode('utf-8'))
    print(imagenes_data)
    return jsonify(imagenes_data)


# Petición para eliminar todas las imagenes de un producto. 
@imagen.route('/imagen/producto/<id>', methods=['DELETE'])
def elimina_imagenes_producto(id):
    return "perrito"