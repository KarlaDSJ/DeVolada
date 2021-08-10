from main import ma

class DireccionEsquema(ma.Schema):
    class Meta:
        fields = ('idDir','correo', 'estado', 'ciudad', 'colonia', 'cp', 'calle', 'numero')