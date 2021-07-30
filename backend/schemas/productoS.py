from main import ma

class ProductoEsquema(ma.Schema):
    class Meta:
        fields = ('id','correo', 'precio', 'nombre', 'descripcion', 'vendidos', 'disponibles')