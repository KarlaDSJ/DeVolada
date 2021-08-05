from main import ma

class OpinarEsquema(ma.Schema):
    class Meta:
        fields = ('correo', 'idProducto', 'opinion', 'calificacion')