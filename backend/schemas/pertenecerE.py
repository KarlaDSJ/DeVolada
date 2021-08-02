from main import ma

class PertenecerEsquema(ma.Schema):
    class Meta:
        fields = ('correo', 'idCarrito')