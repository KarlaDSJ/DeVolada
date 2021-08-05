from main import ma
from marshmallow import fields

class CompraEsquema(ma.Schema):
    class Meta:

        fields = ('idCompra', 'correo', 'idDir', 'numero', 'total')