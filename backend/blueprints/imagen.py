from main import db
from flask import app
from flask import Blueprint, request, jsonify
from models.imagenM import Imagen
from models.productoM import Producto
from schemas.imagenE import ImagenEsquema
from werkzeug.utils import secure_filename
import os

__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@ciencias.unam.mx, omar_gramer@ciencias.unam.mx, kethrimtrad@ciencias.unam.mx, karla_dsj@ciencias.unam.mx, antonioreyes21@ciencias.unam.mx"
__status__ = "Development"

""" 
Archivo de rutas para poder manejar las peticiones para crear la imagen de un producto
"""

imagen = Blueprint('imagen', __name__)

"""---------------- Esquemas ----------------"""

imagen_esquema = ImagenEsquema()
imagen_esquema = ImagenEsquema(many=True)

"""---------------- Rutas ----------------"""

# Límite de imagenes que se pueden subir por producto
IMG_LIMIT = 5

@imagen.route('/imagenes/subir/<idProducto>', methods = ['POST'])
def subir_imagenes(idProducto):
    """
    Agrega una imagen a la base de datos y la guarda en el sistema
    Params:        
        idProducto: identificador del producto
    Returns: ruta de la imágen o un mensaje de error
    """

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


@imagen.route('/imagen', methods=['DELETE'])
def elimina_imagen():
    """
    Eliminar una imagen de la base de datos de un producto
    Params:        
        idProducto: identificador del producto
        imagen: identificador de la imagen
    Returns: mensaje de éxito o de error
    """

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
    """
    Consulta una imagen de la base de datos
    Params:        
        idProducto: identificador del producto
        imagen: identificador de la imagen
    Returns: ruta de la imagen
    """

    imagen = request.json['imagen']
    idProducto = request.json['idProducto']
    imagen_obtenida = db.session.query(Imagen).get((imagen,idProducto))
    return jsonify({"imagen:": imagen_obtenida.imagen})


@imagen.route('/imagen/producto/<id>', methods=['GET'])
def obten_imagenes_producto(id):
    """
    Consulta una imagen de la base de datos
    Params:        
        id: identificador del producto
    Returns: todas las imágenes de un producto
    """
    producto = id
    imagenes_producto = db.session.query(Imagen).filter_by(idProducto=producto)
    return imagen_esquema.jsonify(imagenes_producto)


# Petición para eliminar todas las imagenes de un producto. 
@imagen.route('/imagen/producto/<id>', methods=['DELETE'])
def elimina_imagenes_producto(id):
    """
    Elimina todas las imagenes de un producto
    Params:        
        id: identificador del producto
    Returns: mensaje de error o éxito
    """
    return "perrito"