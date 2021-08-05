from sqlalchemy import desc, func
from main import db
from flask import Blueprint, request, jsonify
from models.productoM import Producto
from models.vendedorM import Vendedor
from models.categoriaM import Categoria
from schemas.productoS import ProductoEsquema

producto = Blueprint('producto', __name__)

"""---------------- Esquemas ----------------"""

producto_esquema = ProductoEsquema()
productos_esquema = ProductoEsquema(many=True)

"""---------------- Rutas ----------------"""

@producto.route('/producto/<id>', methods=['GET'])
def get_producto(id):
    """Nos regresa la información del producto con
     imagenes, sin categoría ni reseñas"""
    producto = db.session.query(Producto).filter_by(idProducto=id).first()

    return producto_esquema.jsonify(producto)

@producto.route('/productos', methods=['GET'])
def get_productos():
    """Nos regresa todos los productos"""
    productos = db.session.query(Producto).all()
 
    return productos_esquema.jsonify(productos)

#Hay que modificar la query si nos mandan una categoría
@producto.route('/producto/buscar', methods=['POST'])
def search_productos():
    """Nos regresa todos los productos que coincidan 
      con el nombre y categoría"""
    categoria = request.json['categoria']
    nombre = request.json['nombre']
    if len(categoria) == 0:
        #buscamos por nombre
        productos = db.session.query(Producto).filter_by(nombre=nombre).all()
    elif len(nombre) == 0:
        #Buscamos por categoria
        productos = db.session.query(Producto).join(Categoria).filter_by(categoria=categoria).all()
    else:
        #Busqueda por nombre y categoria
        productos = db.session.query(Producto).filter_by(nombre=nombre).join(Categoria).filter_by(categoria=categoria).all()
    return productos_esquema.jsonify(productos)

@producto.route('/producto/top5', methods=['GET'])
def top5_productos():
    """Nos regresa los 5 productos más vendidos, si no hay ventas 
    nos regresa los 5 más recientes"""
    ##productos = db.session.query(func.sum(Incluir.cantidad).label('count'), Incluir.producto).group_by(Incluir.producto).order_by(desc('count')).limit(5)
    ##if len(productos) == 0: #Probar que lo de arriba funcione
    productos = db.session.query(Producto).order_by(Producto.idProducto.desc()).limit(5)
    return productos_esquema.jsonify(productos)


@producto.route('/productos/vendedor/<correo>', methods=['GET'])
def obten_productos_vendedor(correo):
    """Nos regresa todos los productos de un vendedor"""
    productos = db.session.query(Producto).filter_by(correo=correo).all()
    return productos_esquema.jsonify(productos)


#Agrega un producto a la base de datos.
@producto.route('/producto', methods=['POST'])
def agrega_producto():    
    """ Agrega un producto a la base de datos
        nos regresa la información del mismo"""
    correo = request.json['correo']
    nombre = request.json['nombre']
    precio = request.json['precio']
    descripcion = request.json['descripcion']
    disponibles = request.json['disponibles']

    if (nombre == ""):
        return jsonify({"error": 101, "mensaje:": "El producto debe tener un nombre."})
    if (precio <= 0):
        return jsonify({"error": 102, "mensaje:": "El precio del producto debe ser mayor a cero."})
    if (descripcion == ""):
        return jsonify({"error": 103, "mensaje:": "El producto debe tener una descripcion."})
    if (disponibles <= 0):
        return jsonify({"error": 104, "mensaje:": "La cantidad de unidades disponibles debe ser mayor a cero."})

    producto_nuevo = Producto(correo, precio, nombre, descripcion, 0, disponibles)

    db.session.add(producto_nuevo)
    db.session.commit()

    return producto_esquema.jsonify(producto_nuevo)


#Actualiza un producto en la base de datos.
@producto.route('/producto/<id>', methods=['PATCH'])
def actualiza_producto(id):    
    producto = db.session.query(Producto).filter_by(idProducto=id).first()

    if (producto is None):
        return jsonify({"mensaje:": "No se puedo actualizar el producto <" + id + "> porque no existe."})

    json_dict = request.get_json(force=True)
    if 'nombre' in json_dict:
        producto.nombre  = request.json['nombre']
    if 'precio' in json_dict:
        producto.precio  = request.json['precio']
    if 'descripcion' in json_dict:
        producto.descripcion  = request.json['descripcion']
    if 'disponibles' in json_dict:
        producto.disponibles  = request.json['disponibles']    
    db.session.commit()
    return producto_esquema.jsonify(producto)


#Elimina un producto de la base de datos.
@producto.route('/producto/<id>', methods=['DELETE'])
def elimina_producto(id):    
    producto_eliminar = db.session.query(Producto).filter_by(idProducto=id).first()

    if (producto is None):
        return jsonify({"mensaje:": "No se puedo eliminar el producto <" + id + "> porque no existe."})

    db.session.delete(producto_eliminar)
    db.session.commit()
    return jsonify({"mensaje:": "Se elimino el producto <" + id + "> correctamente"})
