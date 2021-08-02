from schemas.imagenS import ImagenEsquema
from schemas.categoriaS import CategoriaEsquema
from main import ma
from marshmallow import fields

class ProductoEsquema(ma.Schema):
    """Esquema para el modelo productoM"""
    idProducto = fields.Int()
    correo = fields.Email()
    precio = fields.Float()
    nombre = fields.Str()
    descripcion = fields.Str()
    vendidos = fields.Int()
    disponibles = fields.Int()
    imagenes = fields.List(fields.Nested(ImagenEsquema, only=('imagen',)))
    categoria = fields.List(fields.Nested(CategoriaEsquema, only=('categoria',)))

    class Meta:
        """Formato de salida"""
        fields = ("idProducto", "correo", "precio", "nombre", "descripcion", "vendidos", "disponibles", "imagenes", "categoria")