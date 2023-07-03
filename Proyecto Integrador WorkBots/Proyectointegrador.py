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

#funcion para crear las tablas en la base de datos
def crear_tablas():
    conexion = establecer_conexion()
    if conexion is not None:
        try:
            cursor = conexion.cursor()

            # Crear tabla de productos
            crear_tabla_productos = """
            CREATE TABLE IF NOT EXISTS productos (
                id SERIAL PRIMARY KEY,
                descripcion VARCHAR(100) NOT NULL,
                precio NUMERIC(10, 2) NOT NULL
            )
            """
            cursor.execute(crear_tabla_productos)
            conexion.commit()

            # Crear tabla de clientes
            crear_tabla_clientes = """
            CREATE TABLE IF NOT EXISTS clientes (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL
            )
            """
            cursor.execute(crear_tabla_clientes)
            conexion.commit()

            # Crear tabla de ventas
            crear_tabla_ventas = """
            CREATE TABLE IF NOT EXISTS ventas (
                id SERIAL PRIMARY KEY,
                fecha TIMESTAMP DEFAULT NOW(),
                id_cliente INTEGER REFERENCES clientes (id),
                id_producto INTEGER REFERENCES productos (id),
                cantidad NUMERIC(10, 2) NOT NULL
            )
            """
            cursor.execute(crear_tabla_ventas)
            conexion.commit()

            cursor.close()
            print("Tablas creadas correctamente")

        except (Exception, psycopg2.Error) as error:
            print("Error al crear las tablas:", error)
        finally:
            if conexion is not None:
                conexion.close()
                print("Conexión cerrada")


# Función para obtener precio del producto
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

#funcion para obtener la descripcion del producto
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


# Función para agregar un producto al carrito de compras
def agregar_producto(productos: List[Producto]):
    producto_id = input('Ingrese el id del producto: ')
    descripcion = obtener_descripcion_producto(producto_id)
    precio = obtener_precio_producto(producto_id)
    cantidad = int(input('Ingrese la cantidad del producto: '))
    producto = Producto(descripcion, precio, cantidad)
    productos.append(producto)

#funcion para solicitar indice que se usa para cambiar o borrar producto
def solicitarIndice():
    return int(input("Ingresa el número de producto (el primero es 0): "))

#funcion para cambiar cantidad del producto
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
            producto.subtotal = producto.precio * nuevaCantidad
            productos[indice] = p
    else:
        print("Numero erroneo, producto no encontrado")

#Funcion para quitar productos de la base de datos
def quitarProducto(productos: List[Producto]):
    indice = solicitarIndice()

    if indice < len(productos):
        productos.pop(indice)
    else:
        print("Número erroneo, intente nuevamente")

#Funcion para agregar productos a la base de datos
def AgregarProdBD():
    conexion = establecer_conexion()
    try:
        with conexion:
            with conexion.cursor() as cursor:

                sentencia = 'INSERT INTO productos (descripcion, precio) VALUES (%s, %s) ' # Placeholder
                valores = (input("Ingreso de producto nuevo\nIngrese nombre de producto: "), input('Ingrese precio del producto: ')) #es una tupla
                cursor.execute(sentencia, valores) # De esta manera ejecutamos la sentencia
                # conexion.commit() # esto no lo vamos a usar, se utiliza para guardar los cambios en la base de datos
                registros_insertados = cursor.rowcount # Recupera todos los registros de la sentencia, que seran una lista
                print(f'Los registros insertados son: {registros_insertados}')
    except Exception as e:
        print(f'Ocurrio un error: {e}')
    finally:
        conexion.close()


#Funcion para ver los productos cargados a la base de datos
def VerProdBD():
    conexion = establecer_conexion()
    try:
        with conexion:
            with conexion.cursor() as cursor:

                sentencia = 'SELECT * FROM productos ' # Placeholder
                cursor.execute(sentencia) # De esta manera ejecutamos la sentencia
                registros_leidos = cursor.fetchall()
                print(f'Los registros leidos son: {registros_leidos}')
    except Exception as e:
        print(f'Ocurrio un error: {e}')
    finally:
        conexion.close()

#Funcion para borrar los productos de la base de datos
def BorrarProdBD():
    conexion = establecer_conexion()
    try:
        with conexion:
            with conexion.cursor() as cursor:

                sentencia = 'DELETE FROM productos WHERE id = %s ' # Placeholder
                entrada = input('Digite el numero de valores de registro a eliminar: ')
                valores = (entrada,)  # es una tupla de valores
                cursor.execute(sentencia, valores)  # De esta manera ejecutamos la sentencia
                registros_eliminados = cursor.rowcount
                print(f'El producto eliminado es: {registros_eliminados}')
    except Exception as e:
        print(f'Ocurrio un error: {e}')
    finally:
        conexion.close()

#funcion de impresion de ticket para compra en efectivo
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

#funcion de impresion de ticket para compra en debito
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

#funcion de impresion de ticket para compra en credito
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


# Función del programa ticketera
def TicketeraMain():
    productos = []
    while True:
        nombre = input("***¡¡Bienvenidos al supermercado WorkBots!!***\n\nPor favor, escriba su nombre: ")
        insertar_cliente(nombre)
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
            print("-" * 106)
            print("-" * 106)
        elif fin == "2":
            print("Gracias por visitar el supermercado WorkBots!")
            break
        else:
            print("Opción no válida!")

#Funcion principal de menu para ticketera y base de datos
def MenuPrincipal():
    while True:
        print(" ")
        print(" ")
        print("-" * 106)
        print("***¡¡Bienvenido al sistema de supermercado WorkBots!!*** ")
        print("\nElija su opción:")
        print("1. Crear tablas para la base de datos de: productos, clientes y ventas")
        print("2. Agregar productos a la base de datos")
        print("3. Ver productos en la base de datos")
        print("4. Eliminar producto de la base de datos")
        print("5. Ir al programa de Ticketera")
        print("6. Salir")

        eleccion = input("Seleccione: ")
        if eleccion == "1":
            crear_tablas()
        elif eleccion == "2":
            AgregarProdBD()
        elif eleccion == "3":
            VerProdBD()
        elif eleccion == "4":
            BorrarProdBD()
        elif eleccion == "5":
            TicketeraMain()
        elif eleccion == "6":
            print("-" * 106)
            break
        else:
            print("Opción no válida!")


if __name__ == "__main__":
    MenuPrincipal()
