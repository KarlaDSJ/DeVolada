from main import db
from flask import Blueprint, request, jsonify
from models.categoriaM import Categoria
from schemas.categoriaS import CategoriaEsquema


categoria = Blueprint('categoria', __name__)

categoria_esquema = CategoriaEsquema()
categorias_esquema = CategoriaEsquema(many=True)


# Petición para agregar una categoría a la base de datos.
"""@categoria.route('/categoria', methods=['POST'])
def agrega_categoria():
    categoria  = request.json['categoria']
    idProducto = request.json['idProducto']

    categoria_nueva = Categoria(categoria, idProducto)

    db.session.add(categoria_nueva)
    db.session.commit()

    return jsonify({"mensaje:": "Se agregó la categoría correctamente"})


# Petición para eliminar una categoría de la base de datos a través de su PK. 
@categoria.route('/categoria', methods=['DELETE'])
def elimina_categoria():
    categoria  = request.json['categoria']
    idProducto = request.json['idProducto']

    categoria_eliminar = db.session.query(Categoria).get((categoria,idProducto))

    db.session.delete(categoria_eliminar)
    db.session.commit()

    return jsonify({"mensaje:": "Se eliminó la categoría correctamente"})


# Petición para consultar una categoría de la base de datos a través de su PK. 
@categoria.route('/categoria', methods=['GET'])
def obtener_categoria():
    categoria = request.json['categoria']
    idProducto = request.json['idProducto']

    categoria_obtenida = db.session.query(Categoria).get((categoria,idProducto))
    
    return jsonify({"categoria:": categoria_obtenida.categoria})"""


@categoria.route('/categorias', methods=['GET'])
def obtener_categoria():
    """Función para obtener todas las categorías"""

    categoria_obtenida = db.session.query(Categoria.categoria).distinct()
    
    return categorias_esquema.jsonify(categoria_obtenida)