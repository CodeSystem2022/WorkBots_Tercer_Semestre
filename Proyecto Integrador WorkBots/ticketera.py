from typing import List




class Producto:
    def __init__(self, descripcion: str, precio: float, cantidad: float):
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad
        self.subtotal = precio * cantidad


def agregarProducto(productos: List[Producto]):
    descripcion = input("Ingrese la descripción del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = float(input("Ingrese la cantidad del producto: "))
    producto = Producto(descripcion, precio, cantidad)
    productos.append(producto)


def cambiarCantidad(productos: List[Producto]):
    descripcion = input("Ingrese la descripción del producto a modificar: ")
    nueva_cantidad = float(input("Ingrese la nueva cantidad: "))
    for producto in productos:
        if producto.descripcion == descripcion:
            producto.cantidad = nueva_cantidad
            producto.subtotal = producto.precio * producto.cantidad
            return
    print("Producto no encontrado.")


def quitarProducto(productos: List[Producto]):
    descripcion = input("Ingrese la descripción del producto a quitar: ")
    for producto in productos:
        if producto.descripcion == descripcion:
            productos.remove(producto)
            return
    print("Producto no encontrado.")


def mostrarTicketEfe(productos: List[Producto]):
    total = sum(p.subtotal for p in productos)
    print("\n--- Ticket de compra ---")
    for p in productos:
        print(f"{p.descripcion}: {p.cantidad} x {p.precio} = {p.subtotal}")
    print(f"Total: {total}")


def mostrarTicketDebit(productos: List[Producto]):
    mostrarTicketEfe(productos)


def mostrarTicketCred(productos: List[Producto]):
    mostrarTicketEfe(productos)


def menu():
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
    menu()