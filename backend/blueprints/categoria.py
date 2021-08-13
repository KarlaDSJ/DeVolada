from main import db
from flask import Blueprint, request, jsonify
from models.categoriaM import Categoria
from models.productoM import Producto
from schemas.categoriaE import CategoriaEsquema


categoria = Blueprint('categoria', __name__)

categoria_esquema = CategoriaEsquema()
categorias_esquema = CategoriaEsquema(many=True)


@categoria.route('/categoria/agrega/<idProducto>', methods=['POST'])
def agrega_categorias(idProducto):
    """Función para agregar una lista de categorías a un producto"""
    
    # Verifica que el producto exista
    producto = db.session.query(Producto).filter_by(idProducto=idProducto).first()
    if (producto is None):
        return jsonify({"error": 101, 
                        "mensaje": "El producto <" + str(idProducto) + "> no existe."})

    # Obtiene las nuevas categorias
    categorias_nuevas = request.json['categorias']
    categorias_msj = [] # Lista para regresar categorias en el mensaje

    # Agrega las nuevas categorias
    for categoria in categorias_nuevas:
        categoria = categoria.lower().strip() # Convertir en minisculas y eliminar espacios
        if categoria == "":
            return jsonify({"error": 102, "mensaje": "Se intento agregar una categoria vacia."})
        categorias_msj.append(categoria)
        categoria_no_existe = db.session.query(Categoria).get((categoria,idProducto)) is None
        if categoria_no_existe:
            categoria_nueva = Categoria(categoria, idProducto)
            db.session.add(categoria_nueva)
        else:
            return jsonify({"error": 103, "mensaje": "La categoria <" + categoria + "> ya existe en el producto <" + str(idProducto) + ">."})
    
    # Guarda los cambios en la BD
    db.session.commit()

    return jsonify({"mensaje:": "Se agregaron las categorías <" + 
                    ", ".join(categorias_msj) + "> en el producto <" + str(idProducto) + ">"})


@categoria.route('/categoria/actualiza/<idProducto>', methods=['POST'])
def actualiza_categorias(idProducto):
    """Función para cambiar las categorías de un producto remplazando las anteriores"""
    
    # Verifica que el producto exista
    producto = db.session.query(Producto).filter_by(idProducto=idProducto).first()
    if (producto is None):
        return jsonify({"error": 101, 
                        "mensaje": "El producto <" + str(idProducto) + "> no existe."})

    # Borra las categorias existentes
    categorias_producto = db.session.query(Categoria).filter_by(idProducto=idProducto).all()
    print(categorias_producto)
    for categoria in categorias_producto:
        db.session.delete(categoria)

    # Obtiene las nuevas categorias
    categorias_nuevas = request.json['categorias']
    categorias_msj = [] # Lista para regresar categorias en el mensaje

    # Agrega las nuevas categorias
    for categoria in categorias_nuevas:
        categoria = categoria.lower().strip() # Convertir en minisculas y eliminar espacios
        if categoria == "":
            return jsonify({"error": 102, "mensaje": "Se intento agregar una categoria vacia."})
        categorias_msj.append(categoria)
        categoria_no_existe = db.session.query(Categoria).get((categoria,idProducto)) is None
        if categoria_no_existe:
            categoria_nueva = Categoria(categoria, idProducto)
            db.session.add(categoria_nueva)

    # Guarda los cambios en la BD
    db.session.commit()

    return jsonify({"mensaje:": "Se actualizaron las categorías del producto <" + str(idProducto) + 
                    "> a <" + ", ".join(categorias_msj) + ">"})


@categoria.route('/categoria/elimina/<idProducto>', methods=['DELETE'])
def elimina_categoria(idProducto):
    """Función para eliminar una categoría de un producto"""
    categoria  = request.json['categoria']
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
