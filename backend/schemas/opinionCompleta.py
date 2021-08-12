from main import ma

class OpinarCompletaEsquema(ma.Schema):
    class Meta:
        fields = ('correo','nombre', 'telefono', 'contrasenia','correo' ,'idProducto', 'opinion', 'calificacion')