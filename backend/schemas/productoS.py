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
    #imagenes = fields.Nested(ImagenEsquema, only=('imagen',), many=True)
    imagenes = fields.Nested(ImagenEsquema, only=('imagen',))

    class Meta:
        fields = ("id", "correo", "precio", "nombre", "descripcion", "vendidos", "disponibles", "imagenes")
