from main import ma

class ImagenEsquema(ma.Schema):
    class Meta:
        fields = ('imagen', 'idProducto')