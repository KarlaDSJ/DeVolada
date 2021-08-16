from main import ma
from marshmallow import fields

class ImagenEsquema(ma.Schema):

   class Meta:
      """Formato de salida"""
      fields = ("idImagen","imagen","idProducto")

