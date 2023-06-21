class Producto{
    static contadorProductos = 0;
    constructor(nombre, precio){
        this._idProductos = ++Producto.contadorProductos;
        this._nombre = nombre;
        this._precio = precio;
    }

    get idProductos(){
        return this._idProductos;
    }

    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }
    
    get precio(){
        return this._precio;
    }

    set precio(precio){
        this._precio = precio;
    }

    toString(){
        return `idproductos: ${this._idProductos}, nombre: ${this._nombre}, precio: $${this._precio}`;
    }
}//Fin clase Producto

class Orden{
    static contadorOrdenes = 0;
    static getMAX_PRODUCTOS(){//simula una constante
        return 5;
    }

    constructor(){
        this._idOrden = ++Orden.contadorOrdenes;
        this._productos = [];
        this.contadorProductosAgregados = 0;
    }

    get idOrden(){
        return this._idOrden;
    }

    agregarProducto(producto){
        if(this._productos.length < Orden.getMAX_PRODUCTOS()){
            this._productos.push(producto); //tenemos 2 tipos de sintaxis: 1
            //this._productos[this.contadorProductosAgregados++] = producto; // segunda sintaxis
        }
        else{
            console.log('Nose pueden agregar mas productos');
        }
    }// Fin del metodo agregarProducto

    calcularTotal(){
        let totalVenta = 0;
        for(let producto of this._productos){
            totalVenta += producto.precio;
        }//Fin ciclo for
        return totalVenta;
    }//Fin del metodo calcularTotal

    mostrarOrden(){
        let productosOrden = ' ';
        for(let producto of this._productos){
            productosOrden += '\n{ '+producto.toString()+' }';
        }//fin ciclo for
        console.log(`Orden: ${this.idOrden}, Total: $${this.calcularTotal()}, Productos: ${productosOrden}`);
    }//Fin metodo mostrarOrden
}//Fin de la clase Orde


let producto1 = new Producto('Pantalon', 2000);
let producto2 = new Producto ('Remera', 1500);
let producto3 = new Producto('Cinturon', 500);
let orden1 = new Orden();
let orden2 = new Orden();
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden1.agregarProducto(producto3);
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden2.agregarProducto(producto3);
orden1.mostrarOrden();
orden2.mostrarOrden();