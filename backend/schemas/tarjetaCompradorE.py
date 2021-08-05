from main import ma
from marshmallow import fields

class TarjetaCompradorEsquema(ma.Schema):    
    class Meta:
        fields = ['numero']