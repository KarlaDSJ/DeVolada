from main import db
from flask import Blueprint, request, jsonify
from models.categoriaM import Categoria
from schemas.categoriaE import CategoriaEsquema


categoria = Blueprint('categoria', __name__)

categoria_esquema = CategoriaEsquema()
categoria_esquema = CategoriaEsquema(many=True)


# Petición para agregar una categoría a la base de datos.
@categoria.route('/categoria', methods=['POST'])
def agrega_categoria():
    categoria  = request.json['categoria']
    idProducto = request.json['idProducto']
    categoria_nueva = Categoria(categoria, idProducto)
    db.session.add(categoria_nueva)
    db.session.commit()
    return jsonify({"mensaje:": "Se agregó la categoría <" + categoria + "> en el producto <" + idProducto + "> correctamente"})


# Petición para eliminar una categoría de la base de datos a través de su PK. 
@categoria.route('/categoria', methods=['DELETE'])
def elimina_categoria():
    categoria  = request.json['categoria']
    idProducto = request.json['idProducto']
    categoria_eliminar = db.session.query(Categoria).get((categoria,idProducto))
    db.session.delete(categoria_eliminar)
    db.session.commit()
    return jsonify({"mensaje:": "Se elimino la categoría <" + categoria + "> del producto <" + idProducto + "> correctamente"})


# Petición para consultar las categorías de un producto.
@categoria.route('/categoria/producto/<id>', methods=['GET'])
def obten_categorias_producto(id):
    idProducto = id
    categorias_producto= db.session.query(Categoria).filter_by(idProducto=idProducto)
    
    return categoria_esquema.jsonify(categorias_producto)