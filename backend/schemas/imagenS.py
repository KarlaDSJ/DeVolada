from main import ma
from marshmallow import fields

class ImagenEsquema(ma.Schema):
   imagen = fields.Str() 
   idProducto = fields.Str() 
   class Meta:
        fields = ("idProducto", "imagen")