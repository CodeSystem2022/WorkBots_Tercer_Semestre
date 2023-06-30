class Producto:
    def __init__(self, precio, descripcion, cantidad):
        self.cantidad = cantidad
        self.precio = precio
        self.descripcion = descripcion

    def getSubtotal(self):
        return self.cantidad * self.precio

    def getPrecio(self):
        return self.precio

    def getCantidad(self):
        return self.cantidad

    def setCantidad(self, cantidad):
        self.cantidad = cantidad

    def getDescripcion(self):
        return self.descripcion
