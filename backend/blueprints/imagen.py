from main import db
from flask import Blueprint, request, jsonify
from models.imagenM import Imagen
from schemas.imagenE import ImagenEsquema


imagen = Blueprint('imagen', __name__)

imagen_esquema = ImagenEsquema()
imagen_esquema = ImagenEsquema(many=True)


# Petición para agregar una imagen a la base de datos.
@imagen.route('/imagen', methods=['POST'])
def agrega_imagen():
    imagen = request.json['imagen']
    idProducto = request.json['idProducto']
    imagen_nueva = Imagen(imagen, idProducto)
    db.session.add(imagen_nueva)
    db.session.commit()
    return jsonify({"mensaje:": "Se subió la imagen correctamente"})


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
    imagenes_producto = db.session.query(Imagen).filter_by(idProducto=producto)
    return imagen_esquema.jsonify(imagenes_producto)


# Petición para eliminar todas las imagenes de un producto. 
@imagen.route('/imagen/producto/<id>', methods=['DELETE'])
def elimina_imagenes_producto(id):
    return "perrito"