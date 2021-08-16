from main import ma

class DireccionEsquema(ma.Schema):
    """ Crea un esquema para la dirección del comprador y 
    del vendedor
    """
    class Meta:
        fields = ('idDir','correo', 'estado', 'ciudad', 'colonia', 'cp', 'calle', 'numero')