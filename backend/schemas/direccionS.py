from main import ma

class DireccionEsquema(ma.Schema):
    class Meta:
        fields = ('correo', 'estado', 'ciudad', 'colonia', 'cp', 'calle', 'numero')