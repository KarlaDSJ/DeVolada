from main import ma

class OpinarCompletaEsquema(ma.Schema):
    """ Crea un esquema para dar formato a la opinión
    de un producto con los datos del comprador
    """
    class Meta:
        fields = ('correo','nombre', 'telefono', 'contrasenia','correo' ,'idProducto', 'opinion', 'calificacion')