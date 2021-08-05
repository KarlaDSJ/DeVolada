from main import ma
from marshmallow import fields

class DireccionCompradorEsquema(ma.Schema):    
    class Meta:
        fields = ['idDir', 'correo', 'estado', 'ciudad', 'colonia', 'cp', 'calle', 'numero']