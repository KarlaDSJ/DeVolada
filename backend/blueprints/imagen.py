from main import db
from flask import Blueprint, request, jsonify
from models.imagenM import Imagen
from schemas.imagenS import ImagenEsquema


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
    imagen  = request.json['imagen']

    imagen_eliminada = db.session.query(Imagen).get(imagen)

    db.session.delete(imagen_eliminada)
    db.session.commit()

    return jsonify({"mensaje:": "Se eliminó la categoría correctamente"})


# Petición para consultar una imagen de la base de datos a través de su PK. 
@imagen.route('/imagen', methods=['GET'])
def obtener_imagen():
    imagen = request.json['imagen']
    idProducto = request.json['idProducto']

    imagen_obtenida = db.session.query(Imagen).get((imagen,idProducto))
    
    return jsonify({"imagen:": imagen_obtenida.imagen})