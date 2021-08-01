from main import ma

class ProductoEsquema(ma.Schema):
    class Meta:
        fields = ('idProducto','correo', 'precio', 'nombre', 'descripcion', 'vendidos', 'disponibles')