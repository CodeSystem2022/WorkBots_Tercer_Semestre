from typing import List

import psycopg2

import datetime




class Producto:
    def __init__(self, descripcion: str, precio: int, cantidad: int):
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad
        self.subtotal = precio * cantidad


# Función para establecer la conexión a la base de datos
def establecer_conexion():
    try:
        conexion = psycopg2.connect(
            host="127.0.0.1",
            database="Ticketera",
            user="postgres",
            password="admin"
        )
        print("Conexión establecida correctamente")
        return conexion
    except (Exception, psycopg2.Error) as error:
        print("Error al conectar a la base de datos:", error)



# Función para insertar un producto en la base de datos
def obtener_precio_producto(producto_id):
    conexion = establecer_conexion()
    if conexion is not None:
        try:
            cursor = conexion.cursor()
            # consultar el precio del producto en la bd

            cursor.execute("SELECT precio FROM productos WHERE id = %s", (producto_id))
            result = cursor.fetchone()
            if result:
                precio = int(result[0])
                return precio
            else:
                return None
        except (Exception, psycopg2.Error) as error:
            print("Error en la busqueda de precio de producto: ", error)
        finally:
            if conexion is not None:
                conexion.close()
                print("Conexión cerrada")


def obtener_descripcion_producto(producto_id):
    conexion = establecer_conexion()

    if conexion is not None:
        try:
            cursor = conexion.cursor()
            # consultar el precio del producto en la bd
            cursor.execute("SELECT descripcion FROM productos WHERE id = %s", (producto_id))
            result = cursor.fetchone()
            if result:
                descripcion = result[0]
                return descripcion
            else:
                return None
        except (Exception, psycopg2.Error) as error:
            print("Error en la busqueda de descripcion de producto: ", error)
        finally:
            if conexion is not None:
                conexion.close()
                print("Conexión cerrada")


'''
# Función para insertar un cliente en la base de datos
def insertar_cliente(nombre):
    conexion = establecer_conexion()
    if conexion is not None:
        try:
            cursor = conexion.cursor()

            insertar_cliente = """
            INSERT INTO clientes (nombre)
            VALUES (%s)
            """
            cursor.execute(insertar_cliente, (nombre,))
            conexion.commit()

            cursor.close()
            print("Cliente insertado correctamente")
        except (Exception, psycopg2.Error) as error:
            print("Error al insertar el cliente:", error)
        finally:
            if conexion is not None:
                conexion.close()
                print("Conexión cerrada")


# Función para insertar una venta en la base de datos
def insertar_venta(id_cliente, id_producto, cantidad):
    conexion = establecer_conexion()
    if conexion is not None:
        try:
            cursor = conexion.cursor()

            insertar_venta = """
            INSERT INTO ventas (id_cliente, id_producto, cantidad)
            VALUES (%s, %s, %s)
            """
            cursor.execute(insertar_venta, (id_cliente, id_producto, cantidad))
            conexion.commit()

            cursor.close()
            print("Venta registrada correctamente")
        except (Exception, psycopg2.Error) as error:
            print("Error al registrar la venta:", error)
        finally:
            if conexion is not None:
                conexion.close()
                print("Conexión cerrada")
'''


# Función para agregar un producto al carrito de compras
def agregar_producto(productos: List[Producto]):
    producto_id = input('Ingrese el id del producto: ')
    descripcion = obtener_descripcion_producto(producto_id)
    precio = obtener_precio_producto(producto_id)
    cantidad = int(input('Ingrese la cantidad del producto: '))
    producto = Producto(descripcion, precio, cantidad)
    productos.append(producto)

def solicitarIndice():
    return int(input("Ingresa el número de producto (el primero es 0): "))


def cambiarCantidad(productos: List[Producto]):
    indice = solicitarIndice()
    #descripcion = input("Ingrese la descripción del producto a modificar: ")
    #nueva_cantidad = float(input("Ingrese la nueva cantidad: "))
    #for producto in productos:
    #    if producto.descripcion == descripcion:
    #        producto.cantidad = nueva_cantidad
    #        producto.subtotal = producto.precio * producto.cantidad
    #        return
    #print("Producto no encontrado.")

    if indice < len(productos):
        for producto in productos:
            p = productos[indice]
            nuevaCantidad = float(input("Ingrese nueva Cantidad: "))
            producto.cantidad = nuevaCantidad
            producto.subtotal = producto.precio
            productos[indice] = p
    else:
        print("Numero erroneo, producto no encontrado")



def quitarProducto(productos: List[Producto]):
    indice = solicitarIndice()

    if indice < len(productos):
        productos.pop(indice)
    else:
        print("Número erroneo, intente nuevamente")



def mostrarTicketEfe(productos: List[Producto]):
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

    total = sum(p.subtotal for p in productos)

    for p in productos:
        print("|{:20s}|{:20f}|{:20f}|{:20f}|".format(p.descripcion, p.cantidad, p.precio,  p.subtotal))

    print("-" * 85)
    print("|%83s|" % ("Total: " + str(total)))
    print("|%83s|" % ("Impuestos: " + str(total - total / 1.21)))

def mostrarTicketDebit(productos: List[Producto]):
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
    print("Condicion de venta: Debito")
    print("-" * 106)
    print("Ticket factura B")
    print("Consumidor final")
    print("-" * 106)
    print(" ")
    print("|%-20s|%-20s|%-20s|%-20s|" % ("Descripción", "Precio", "Cantidad", "Subtotal"))
    print("-" * 85)
    total = 0
    total = sum(p.subtotal for p in productos)
    for p in productos:
        print("|{:20s}|{:20f}|{:20f}|{:20f}|".format(p.descripcion, p.cantidad, p.precio, p.subtotal))
    print("-" * 85)
    print("|%83s|" % ("Total: " + str(total)))
    print("|%83s|" % ("Impuestos: " + str(total - total / 1.21)))

def mostrarTicketCred(productos: List[Producto]):
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
    print("Condicion de venta: Tarjeta de Débito")
    print("-" * 106)
    print("Ticket factura B")
    print("Consumidor final")
    print("-" * 106)
    print(" ")
    print("|%-20s|%-20s|%-20s|%-20s|" % ("Descripción", "Precio", "Cantidad", "Subtotal"))
    print("-" * 85)
    total = 0
    total = sum(p.subtotal for p in productos)
    for p in productos:
        print("|{:20s}|{:20f}|{:20f}|{:20f}|".format(p.descripcion, p.cantidad, p.precio, p.subtotal))
    print("-" * 85)
    print("|%83s|" % ("Total: " + str(total)))
    print("|%83s|" % ("Impuestos: " + str(total - total / 1.21)))

# Función principal del programa
def main():
    productos = []
    while True:
        nombre = input("***¡¡Bienvenidos al supermercado WorkBots!!***\n\nPor favor, escriba su nombre: ")
        while True:
            if productos:
                print("\n" + "-" * 106)
                print("|{:22s}|{:22s}|{:22s}|{:22s}|".format("Descripción", "Precio", "Cantidad", "Subtotal"))
                print("-" * 106)
                for p in productos:
                    print("|{:22s}|{:22f}|{:22f}|{:22f}|".format(p.descripcion, p.precio, p.cantidad, p.subtotal))
                print("-" * 106)

            print("\n¡Bienvenido {}!".format(nombre))
            print("\nElija su opción:")
            print("1. Agregar producto")
            print("2. Cambiar cantidad")
            print("3. Quitar producto")
            print("4. Mostrar ticket y terminar venta")
            print("5. Salir")

            eleccion = input("Seleccione: ")

            if eleccion == "1":

                agregar_producto(productos)
            elif eleccion == "2":
                cambiarCantidad(productos)
            elif eleccion == "3":
                quitarProducto(productos)
            elif eleccion == "4":
                if len(productos)!=0 :
                        eleccionPago = input("Por favor, seleccione el método de pago:\n"
                                     "1. Efectivo\n"
                                     "2. Tarjeta débito\n"
                                     "3. Tarjeta crédito\n"
                                     "4. Volver al menú anterior\n"
                                     "5. Salir\n"
                                     "Seleccione: ")
                        if eleccionPago == "1":
                            mostrarTicketEfe(productos)
                            print("Gracias por su compra, {}!!".format(nombre))
                            break
                        elif eleccionPago == "2":
                            mostrarTicketDebit(productos)
                            print("Gracias por su compra, {}!!".format(nombre))
                            break
                        elif eleccionPago == "3":
                            mostrarTicketCred(productos)
                            print("Gracias por su compra, {}!!".format(nombre))
                            break
                        elif eleccionPago == "4":
                            print("Volviendo...")
                        elif eleccionPago == "5":
                            break
                        else:
                            print("Opción no válida!")
                else:
                    print('Debe agregar al menos un articulo!')

            elif eleccion == "5":
                break
            else:
                print("Opción no válida!")

        fin = input("¿Nuevo Cliente? ¿Desea continuar?\n"
                    "1. Si\n"
                    "2. No\n"
                    "Seleccione: ")
        if fin == "1":
            productos.clear()
            print("Volviendo...")
        elif fin == "2":
            print("Gracias por visitar el supermercado WorkBots!")
            break
        else:
            print("Opción no válida!")


if __name__ == "__main__":
    main()
