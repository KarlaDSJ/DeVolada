from schemas.imagenS import ImagenEsquema
from main import ma
from marshmallow import fields

class ProductoEsquema(ma.Schema):
    id = fields.Int()
    correo = fields.Email()
    precio = fields.Float()
    nombre = fields.Str()
    descripcion = fields.Str()
    vendidos = fields.Int()
    disponibles = fields.Int()
    fotos = fields.Nested(ImagenEsquema, many=True, only=('imagen',))

    class Meta:
        fields = ("id", "correo", "precio", "nombre", "descripcion", "vendidos", "disponibles", "fotos")
