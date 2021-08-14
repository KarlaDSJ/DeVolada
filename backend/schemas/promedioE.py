from main import ma

class Promedio(ma.Schema):
    class Meta:
        fields = ('idProducto','avg(calificacion)')