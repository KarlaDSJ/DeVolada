from main import ma

class TarjetaCompradorEsquema(ma.Schema):
    """ Crea un esquema para la tarjeta de un
    comprador, solo muestra el número
    descifrado de la tarjeta """
    class Meta:
        fields = ['numero']