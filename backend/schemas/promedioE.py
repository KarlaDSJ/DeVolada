from main import ma

class Promedio(ma.Schema):
    """ Crea un esquema para dar formato a la calificación 
    de las opiniones
    """
    class Meta:
        fields = ('idProducto','avg(calificacion)')