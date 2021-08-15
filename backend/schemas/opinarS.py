from main import ma

class OpinarEsquema(ma.Schema):
    """ Crea un esquema para dar formato a la opinión
    de un producto
    """
    class Meta:
        fields = ('correo', 'idProducto', 'opinion', 'calificacion')