from main import ma
from marshmallow import fields

class DireccionCompradorEsquema(ma.Schema):
    """ Inicia un esquema para la dirección de
    un comprador. Incluye el identificador
    de la misma, el correo del comprador,
    estado, ciudad/delegación, ciudad, colonia,
    código postal, calle y número """
    class Meta:
        fields = ['idDir', 'correo', 'estado', 'ciudad', 'colonia', 'cp', 'calle', 'numero']