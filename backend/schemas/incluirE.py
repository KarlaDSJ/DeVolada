from main import ma
from marshmallow import fields

class IncluirEsquema(ma.Schema):
    """ Inicia un esquema para la relación incluir,
    contiene el identificador de la compra, del
    producto y la cantidad del producto adquirida
    """
    class Meta:
        fields = ('idCompra', 'idProducto', 'cantidad')