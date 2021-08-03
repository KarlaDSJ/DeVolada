from main import ma
from schemas.productoS import ProductoEsquema
from marshmallow import fields

class CarritoEsquema(ma.Schema):
    productos = fields.List(fields.Nested(ProductoEsquema, only=("idProducto",)))

    class Meta:
        fields = ['idCarrito', 'productos']