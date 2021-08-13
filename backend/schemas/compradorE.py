from main import ma

class CompradorEsquema(ma.Schema):
    """ Crea un esquema para un comprador.
    Inclueye su correo, nombre, teléfono 
    y contraseña hasheada """    
    class Meta:
        fields = ('correo', 'nombre', 'telefono', 'contrasenia')