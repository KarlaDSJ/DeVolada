from main import ma
from marshmallow import fields

class IncluirEsquema(ma.Schema):
    class Meta:

        fields = ('idCompra', 'idProducto', 'cantidad')