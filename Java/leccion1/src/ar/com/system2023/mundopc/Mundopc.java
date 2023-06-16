package ar.com.system2023.mundopc;


public class Mundopc {
     public static void main(String[] args){
        Monitor monitorHP =new Monitor ("HP", 13); // IMPORTAR LA CLASE
        Teclado tecladoHP = new Teclado("Bluetooth", "HP");
        Raton ratonHP = new Raton("Bluetooth", "HP");
        Computadora computadoraHP = new Computadora ("Computadora HP", monitorHP,tecladoHP,ratonHP);
        
        //Creamos otro objeto de diferente marca
        Monitor monitorGamer = new Monitor("Gamer",32);
        Teclado tecladoGamer =new Teclado ("Bluetooth", "Gamer");
        Raton  ratonGamer = new Raton ("Bluetooth", "Gamer");
        var computadoraGamer = new Computadora ("computadora Gamer",monitorGamer,tecladoGamer,ratonGamer);
        Orden orden1;
         orden1 = new Orden();
         Orden orden2 = new Orden();
        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(computadoraGamer);
        
        Computadora computadorasVarias = new Computadora("Computadora de varias marcas", monitorHP,tecladoGamer,ratonHP);
        orden2.agregarComputadora(computadorasVarias);
        orden1.mostrarOrden();
        orden2.mostrarOrden();
        
     }
                
} 
   
    
            