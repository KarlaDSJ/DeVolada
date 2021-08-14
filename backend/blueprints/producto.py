from sqlalchemy import desc, func
from sqlalchemy.sql.expression import true
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



#Agrega un registro de producto a la base de datos.
@producto.route('/producto', methods=['POST'])
def agrega_producto():    
    """ Agrega un producto a la base de datos
        nos regresa la información del mismo"""
    correo = request.json['correo']
    nombre = request.json['nombre'].strip()
    precio = request.json['precio']
    descripcion = request.json['descripcion'].strip()
    disponibles = request.json['disponibles']

    # Valida que los datos recibidos sean correctos
    validacion = valida_datos(correo,nombre,precio,descripcion,disponibles)
    if(not validacion["correcto"]): return jsonify(validacion)

    # Agrega el producto a la BD
    producto_nuevo = Producto(correo, precio, nombre, descripcion, 0, disponibles)
    db.session.add(producto_nuevo)
    db.session.commit()

    # Guarda los cambios en la BD
    return producto_esquema.jsonify(producto_nuevo)


#Actualiza un producto en la base de datos.
@producto.route('/producto/<idProducto>', methods=['PATCH'])
def actualiza_producto(idProducto):    
    producto = db.session.query(Producto).filter_by(idProducto=idProducto).first()
    correo = request.json['correo']
    nombre = request.json['nombre'].strip()
    precio = request.json['precio']
    descripcion = request.json['descripcion'].strip()
    disponibles = request.json['disponibles']

    # Verifica que el producto exista en la BD
    if (producto is None):
        return jsonify({"error": 100, "mensaje": "El producto <" + str(idProducto) + "> no existe."})

    # Verifica que los datos recibidos sean correctos
    validacion = valida_datos(correo,nombre,precio,descripcion,disponibles)
    if(not validacion["correcto"]): return jsonify(validacion)

    # Actualiza los valores del producto
    producto.nombre  = request.json['nombre']
    producto.precio  = request.json['precio']
    producto.descripcion  = request.json['descripcion']
    producto.disponibles  = request.json['disponibles']   

    # Guarda los cambios en la BD
    db.session.commit()
    return producto_esquema.jsonify(producto)


#Elimina un registro de producto de la base de datos.
@producto.route('/producto/<idProducto>', methods=['DELETE'])
def elimina_producto(idProducto):    
    producto_eliminar = db.session.query(Producto).filter_by(idProducto=idProducto).first()

    # Verifica que el producto exista en la BD
    if (producto is None):
        return jsonify({"error": 100, "mensaje": "El producto <" + str(idProducto) + "> no existe."})

    # Borra el producto de la BD
    db.session.delete(producto_eliminar)

    # Guarda los cambios en la BDs
    db.session.commit()

    return jsonify({"mensaje": "Se eliminó el producto <" + str(idProducto) + "> correctamente"})


# Verifica que los campos recibidos sean correctos. En caso de fallar
# regresa un json con el mensaje de error.
def valida_datos(correo,nombre,precio,descripcion,disponibles):
    if (correo == ""):
        return {"correcto": False, "error": 101, "mensaje": "No hay un correo asignado a la petición."}
    if (nombre.strip() == ""):
        return {"correcto": False, "error": 102, "mensaje": "El producto debe tener un nombre."}
    if (not (type(precio) == float or type(precio) == int)):
        return {"correcto": False, "error": 103, "mensaje": "El precio del producto debe ser un número."}
    if (precio <= 0):
        return {"correcto": False, "error": 104, "mensaje": "El precio del producto debe ser mayor a cero."}
    if (descripcion.strip() == ""):
        return {"correcto": False, "error": 105, "mensaje": "El producto debe tener una descripcion."}
    if (type(disponibles) != int):
        return {"correcto": False, "error": 106, "mensaje": "La cantidad de unidades disponibles debe ser un número entero."}
    if (disponibles <= 0):
        return {"correcto": False, "error": 107, "mensaje": "La cantidad de unidades disponibles debe ser mayor a cero."}
    return {"correcto": True}
