from main import ma

class PertenecerEsquema(ma.Schema):
    """ Inicia un esquema para la relación pertenecer,
    incluye el correo del comprador y el identificador
    del carrito a asignarse """
    class Meta:
        fields = ('correo', 'idCarrito')