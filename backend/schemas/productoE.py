from main import ma

class ProductoEsquema(ma.Schema):
    class Meta:
        fields = ('correo', 'precio', 'nombre', 'descripcion', 'vendidos', 'disponibles')