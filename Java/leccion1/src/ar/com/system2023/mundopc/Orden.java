 
package ar.com.system2023.mundopc;

public class Orden {
  private final int idOrden;
  private Computadora computadora[]; //arreglo de objetos
  private static int contadorOrdenes;
  private static final int MAX_COMPUTADORA = 10;
  private int contadorComputadora;
    private int i;
  
  
  //constructor vacio
  public Orden(){
      this.idOrden = ++Orden.contadorOrdenes;
      this.computadora= new Computadora[Orden.MAX_COMPUTADORA];
      
  }
      
  // Método para agregar una nueva computadora al arreglo
  public void agregarComputadora(Computadora computadora){
      if (this.contadorComputadora < Orden.MAX_COMPUTADORA){
          this.computadora[this.contadorComputadora++] = computadora;   
      }
      else{
          System.out.println("Has superado el limite: "+Orden.MAX_COMPUTADORA);
          
      }
    }
  
     //moatrarOrden
   
     public void mostrarOrden(){
         System.out.println("orden #: "+this.idOrden);
         System.out.println("Computadora de la orden #: "+ this.idOrden);
         for(int i =0; i< this.contadorComputadora; i++);
            System.out.println(this.computadora[i]);
     }  
     
         
     
  
  
}
