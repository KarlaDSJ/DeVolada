from main import ma

class CategoriaEsquema(ma.Schema):
    class Meta:
        fields = ('categoria', 'idProducto')