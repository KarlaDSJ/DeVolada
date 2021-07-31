from main import ma

class TarjetaEsquema(ma.Schema):
    class Meta:
        fields = ('correo', 'numero', 'duenio', 'fechCad', 'cvv')