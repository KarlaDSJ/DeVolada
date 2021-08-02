from main import ma

class ProductoEsquema(ma.Schema):
    class Meta:
        fields = ('correo', 'total', 'nombre', 'idDir', 'tarjeta')