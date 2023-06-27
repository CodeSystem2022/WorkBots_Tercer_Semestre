import datetime


class Producto:
    def __init__(self, precio, descripcion, cantidad):
        self.precio = precio
        self.descripcion = descripcion
        self.cantidad = cantidad

    def setCantidad(self, nuevaCantidad):
        self.cantidad = nuevaCantidad

    def getDescripcion(self):
        return self.descripcion

    def getPrecio(self):
        return self.precio

    def getCantidad(self):
        return self.cantidad

    def getSubtotal(self):
        return self.precio * self.cantidad


def solicitarProducto():
    descripcion = input("Ingresa descripción: ")
    cantidad = float(input("Ingrese cantidad: "))
    precio = float(input("Ingresa precio: "))
    return Producto(precio, descripcion, cantidad)


def agregarProducto(productos):
    productos.append(solicitarProducto())


def solicitarIndice():
    return int(input("Ingresa el número de producto: "))


def cambiarCantidad(productos):
    indice = solicitarIndice()
    p = productos[indice]
    nuevaCantidad = float(input("Ingrese nueva Cantidad: "))
    p.setCantidad(nuevaCantidad)
    productos[indice] = p


def quitarProducto(productos):
    indice = solicitarIndice()
    if indice < len(productos):
        productos.pop(indice)
    else:
        print("Número erroneo, intente nuevamente")


def mostrarTicketEfe(productos):
    fecha = datetime.datetime.now()
    print("-" * 106)
    print("                                                        Supermercados")
    print("   *        *       *    * * *     * * * *      *    *         * * *      * * *    * * * * *    * * *     ")
    print("    *     *  *     *    *     *    *       *    *   *          *     *   *     *       *       *          ")
    print("     *   *    *   *     *     *    * * *  *     * *            * * * *   *     *       *        * * *     ")
    print("      * *      * *      *     *    *       *    *   *          *     *   *     *       *              *   ")
    print("       *        *        * * *     *       *    *    *         * * *      * * *        *        * * *     ")
    print(" ")
    print("Workbots S. A.")
    print("CUIT: 30-123456789-0")
    print("Domicilio comercial: Av. J. J. Urquiza 314, San Rafael, Mendoza")
    print("IVA Responsable inscripto")
    print(" ")
    print("-" * 106)
    print("Fecha:", fecha)
    print("Condicion de venta: Efectivo")
    print("-" * 106)
    print("Ticket factura B")
    print("Consumidor final")
    print("-" * 106)
    print(" ")
    print("|%-20s|%-20s|%-20s|%-20s|" % ("Descripción", "Precio", "Cantidad", "Subtotal"))
    print("-" * 85)
    total = 0
    for p in productos:
        print("|%-20s|%-20f|%-20f|%-20f|" % (p.getDescripcion(), p.getPrecio(), p.getCantidad(), p.getSubtotal()))
        total += p.getSubtotal()
    print("-" * 85)
    print("|%83s|" % ("Total: " + str(total)))
    print("|%83s|" % ("Impuestos: " + str(total - total / 1.21)))


def mostrarTicketDebit(productos):
    fecha = datetime.datetime.now()
    print("-" * 106)
    print("                                                        Supermercados")
    print("   *        *       *    * * *     * * * *      *    *         * * *      * * *    * * * * *    * * *     ")
    print("    *     *  *     *    *     *    *       *    *   *          *     *   *     *       *       *          ")
    print("     *   *    *   *     *     *    * * *  *     * *            * * * *   *     *       *        * * *     ")
    print("      * *      * *      *     *    *       *    *   *          *     *   *     *       *              *   ")
    print("       *        *        * * *     *       *    *    *         * * *      * * *        *        * * *     ")
    print(" ")
    print("Workbots S. A.")
    print("CUIT: 30-123456789-0")
    print("Domicilio comercial: Av. J. J. Urquiza 314, San Rafael, Mendoza")
    print("IVA Responsable inscripto")
    print(" ")
    print("-" * 106)
    print("Fecha:", fecha)
    print("Condicion de venta: Tarjeta de debito")
    print("-" * 106)
    print("Ticket factura B")
    print("Consumidor final")
    print("-" * 106)
    print(" ")
    print("|%-20s|%-20s|%-20s|%-20s|" % ("Descripción", "Precio", "Cantidad", "Subtotal"))
    print("-" * 85)
    total = 0
    for p in productos:
        print("|%-20s|%-20f|%-20f|%-20f|" % (p.getDescripcion(), p.getPrecio(), p.getCantidad(), p.getSubtotal()))
        total += p.getSubtotal()
    print("-" * 85)
    print("|%83s|" % ("Total: " + str(total)))
    print("|%83s|" % ("Impuestos: " + str(total - total / 1.21)))


def mostrarTicketCred(productos):
    fecha = datetime.datetime.now()
    print("-" * 106)
    print("                                                        Supermercados")
    print("   *        *       *    * * *     * * * *      *    *         * * *      * * *    * * * * *    * * *     ")
    print("    *     *  *     *    *     *    *       *    *   *          *     *   *     *       *       *          ")
    print("     *   *    *   *     *     *    * * *  *     * *            * * * *   *     *       *        * * *     ")
    print("      * *      * *      *     *    *       *    *   *          *     *   *     *       *              *   ")
    print("       *        *        * * *     *       *    *    *         * * *      * * *        *        * * *     ")
    print(" ")
    print("Workbots S. A.")
    print("CUIT: 30-123456789-0")
    print("Domicilio comercial: Av. J. J. Urquiza 314, San Rafael, Mendoza")
    print("IVA Responsable inscripto")
    print(" ")
    print("-" * 106)
    print("Fecha:", fecha)
    print("Condicion de venta: Tarjeta de credito")
    print("-" * 106)
    print("Ticket factura B")
    print("Consumidor final")
    print("-" * 106)
    print(" ")
    print("|%-20s|%-20s|%-20s|%-20s|" % ("Descripción", "Precio", "Cantidad", "Subtotal"))
    print("-" * 85)
    total = 0
    for p in productos:
        print("|%-20s|%-20f|%-20f|%-20f|" % (p.getDescripcion(), p.getPrecio(), p.getCantidad(), p.getSubtotal()))
        total += p.getSubtotal()
    print("-" * 85)
    print("|%83s|" % ("Total: " + str(total)))
    print("|%83s|" % ("Impuestos: " + str(total - total / 1.21)))
