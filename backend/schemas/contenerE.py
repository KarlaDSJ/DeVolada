from main import ma

class ContenerEsquema(ma.Schema):
    class Meta:
        fields = ('idProducto', 'idCarrito', 'cantidad')