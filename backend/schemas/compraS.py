from main import ma

class CompraEsquema(ma.Schema):
    """ Crea un esquema de una compra, ésta incluye el
    identificador de la misma, el correo del comprador
    que la compro, identificador de la dirección de
    envío, el numero de tarjeta con el que fue pagado
    y el total de la compra """
    class Meta:
        fields = ('idCompra', 'correo', 'idDir', 'numero', 'total')