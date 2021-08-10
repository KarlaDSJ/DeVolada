from main import ma

class ContenerEsquema(ma.Schema):
    """ Crea un esquema para la relación contener
    que incluye el identificador del producto,
    el del carrito y la cantidad que se incluye
    """
    class Meta:
        fields = ('idProducto', 'idCarrito', 'cantidad')