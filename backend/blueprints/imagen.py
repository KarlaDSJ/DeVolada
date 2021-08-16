from marshmallow.utils import pprint
from main import db
from flask import app
from flask import Blueprint, request, jsonify
from models.imagenM import Imagen
from models.productoM import Producto
from schemas.imagenE import ImagenEsquema
from werkzeug.utils import secure_filename
from PIL import Image
import os
from pprint import pprint

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
        # Agrega la direccion de la imagen a la BD
        imagen_nueva = Imagen(request.json[i], idProducto)
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
    print(request.json)
    # Verifica que el producto exista
    producto = db.session.query(Producto).filter_by(idProducto=idProducto).first()
    if (producto is None):
        return jsonify({"error": 101, 
                        "mensaje": "No se pudieron borrar las imagenes. " + 
                        "El producto <" + str(idProducto) + "> no existe."})

    # Busca las imagenes existentes en el producto
    imagenes_producto = db.session.query(Imagen).filter_by(idProducto=idProducto).all()

    # Elimina las entradas de las imagenes en la BD
    for img in imagenes_producto:
        db.session.delete(img) # Elimina la entrada en la BD
    db.session.commit()

    # Cuenta las imagenes que se van a subir
    cantidad_imgs_subir = len(request.json)

    # Verifica que no se exceda la cantidad de imagenes permitidas
    if( cantidad_imgs_subir > IMG_LIMIT ):
        return jsonify({"error": 102,
                        "mensaje": "No se pudieron subir las imagenes. Se ha excedido el límite de imagenes (" 
                        + str(cantidad_imgs_subir) + ") para el producto <" + str(idProducto) + ">"})

    # Sube y guarda las nuevas imágenes
    for i in range(cantidad_imgs_subir):
        # Agrega la direccion de la imagen a la BD
        imagen_nueva = Imagen(request.json[i], idProducto)
        db.session.add(imagen_nueva) # Guarda la entrada en la BD

    # Guarda los cambios en la BD
    db.session.commit()

    return jsonify({"mensaje": "Se actualizaron las imagenes del producto <" + str(idProducto) + "> correctamente." })


# Petición para obtener las imagenes en base64 de un producto. 
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

    return imagenes_esquema.jsonify(imagenes_producto)


# Petición para obtener la primer imagen en base64 de un producto. 
@imagen.route('/imagen/producto/<idProducto>', methods=['GET'])
def obten_imagen_producto(idProducto):

    # Verifica que el producto exista
    producto = db.session.query(Producto).filter_by(idProducto=idProducto).first()
    if (producto is None):
        return jsonify({"error": 101, 
                        "mensaje": "No se pudieron obtener las imagenes. " + 
                        "El producto <" + str(idProducto) + "> no existe."})

    # Obtiene las rutas de las imagenes desde la BD
    imagen_producto = db.session.query(Imagen).filter_by(idProducto=idProducto).first()
    return imagen_esquema.jsonify(imagen_producto)


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

    return jsonify({"mensaje:": "Se eliminaron " + str(imagenes_cantidad) 
        + " imagenes del producto <" + str(idProducto) + "> correctamente."})