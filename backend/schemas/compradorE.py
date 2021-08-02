from main import ma

class CompradorEsquema(ma.Schema):
    class Meta:
        fields = ('correo', 'nombre', 'telefono', 'contrasenia')