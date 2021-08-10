from main import db
from flask import Blueprint, request, jsonify
from models.categoriaM import Categoria
from schemas.categoriaE import CategoriaEsquema


categoria = Blueprint('categoria', __name__)

categoria_esquema = CategoriaEsquema()
categorias_esquema = CategoriaEsquema(many=True)


@categoria.route('/categoria', methods=['POST'])
def agrega_categoria():
    """Función para agregar una categoría a un producto"""
    categoria  = request.json['categoria']
    idProducto = request.json['idProducto']
    categoria_nueva = Categoria(categoria, idProducto)

    categoria_nueva = Categoria(categoria, idProducto)

    db.session.add(categoria_nueva)
    db.session.commit()
    return jsonify({"mensaje:": "Se agregó la categoría <" + categoria + "> en el producto <" + str(idProducto) + "> correctamente."})


@categoria.route('/categoria', methods=['DELETE'])
def elimina_categoria():
    """Función para eliminar una categoría de un producto"""
    categoria  = request.json['categoria']
    idProducto = request.json['idProducto']
    categoria_eliminar = db.session.query(Categoria).get((categoria,idProducto))
    if( categoria_eliminar is None):
        return jsonify({"mensaje:": "Error. La <" + categoria + "> del producto <" + str(idProducto) + "> no existe."})
    db.session.delete(categoria_eliminar)
    db.session.commit()
    return jsonify({"mensaje:": "Se elimino la categoría <" + categoria + "> del producto <" + str(idProducto) + "> correctamente."})


@categoria.route('/categoria/producto/<id>', methods=['GET'])
def obten_categorias_producto(id):
    """Función para obtener las categorías de un producto"""
    categorias_producto = db.session.query(Categoria).filter_by(idProducto=id)
    print( categorias_producto)
    return categorias_esquema.jsonify(categorias_producto)


@categoria.route('/categorias', methods=['GET'])
def obtener_todas_las_categorias():
    """Función para obtener todas las categorías existentes en la base de datos"""
    categoria_obtenida = db.session.query(Categoria.categoria).distinct()
    return categorias_esquema.jsonify(categoria_obtenida)
