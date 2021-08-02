from main import ma

class VendedorEsquema(ma.Schema):
    class Meta:
        fields = ('correo', 'nombre', 'telefono', 'contrasenia')