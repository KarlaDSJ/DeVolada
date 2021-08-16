from main import ma

class TarjetaEsquema(ma.Schema):
    """ Crea un esquema para la tarjeta"""
    class Meta:
        fields = ('correo', 'numero', 'duenio', 'fechCad', 'cvv')