from main import ma

class VendedorEsquema(ma.Schema):
    """ Crea un esquema para un Vendedor.
    Incluye su correo, nombre, teléfono 
    y contraseña hasheada """  
    class Meta:
        fields = ('correo', 'nombre', 'telefono', 'contrasenia')