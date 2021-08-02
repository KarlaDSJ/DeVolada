from main import ma
from marshmallow import fields

class CategoriaEsquema(ma.Schema):
   """Esquema para el modelo categoriaM"""
   categoria = fields.Str() 
   idProducto = fields.Str() 

   class Meta:
      """Formato de salida"""
      fields = ("categoria","idProducto")