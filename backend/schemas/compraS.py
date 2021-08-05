from main import ma
from marshmallow import fields

class CompraEsquema(ma.Schema):
    class Meta:

        fields = ('correo', 'idDir', 'numero', 'total')