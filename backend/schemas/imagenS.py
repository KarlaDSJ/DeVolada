from main import ma
from marshmallow import fields

class ImagenEsquema(ma.Schema):
   """Esquema para el modelo imagenM"""
   imagen = fields.Str() 
   idProducto = fields.Str() 

   class Meta:
      """Formato de salida"""
      fields = ("imagen","idProducto")