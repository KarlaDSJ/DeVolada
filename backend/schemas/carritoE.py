from main import ma
from schemas.productoS import ProductoEsquema
from marshmallow import fields


class CarritoEsquema(ma.Schema):
    """ Crea un esquema de un carrito que incluye
    su identificador y una lista con los identificadores
    de los productos comprados y su cantidad """
    productos = fields.List(fields.Nested(ProductoEsquema, only=("idProducto",)))

    class Meta:
        fields = ['idCarrito', 'productos']
