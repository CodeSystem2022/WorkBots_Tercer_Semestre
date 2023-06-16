package test;

import Enumeraciones.Continentes;
import Enumeraciones.Dias;


public class testEnumeraciones {
    public static void main(String[] args) {
        System.out.println(" Dia 1: "+Dias.lunes);
        indicarDiaSemana(Dias.martes);
      System.out.println("Continente No. 1: "+Continentes.AFRICA);
      System.out.println("No. de paises en el 1er. continente: "+Continentes.AFRICA.getPaises());
      System.out.println("No. de habitantes en el 1er.continente:" +Continentes.AFRICA.getHabitantes());
        
      System.out.println("Continente No. 2: "+Continentes.EUROPA);
      System.out.println("No. de paises en el 2do. continente: "+Continentes.EUROPA.getPaises());
      System.out.println("No. de habitantes en el 4to.continente:" +Continentes.EUROPA.getHabitantes()); 
      
      System.out.println("Continente No. 3: "+Continentes.ASIA);
      System.out.println("No. de paises en el 3er. continente: "+Continentes.ASIA.getPaises());
      System.out.println("No. de habitantes en el 3er.continente:" +Continentes.ASIA.getHabitantes());  
      
      System.out.println("Continente No. 4: "+Continentes.AMERICA);
      System.out.println("No. de paises en el 4to. continente: "+Continentes.AMERICA.getPaises());
      System.out.println("No. de habitantes en el 4to.continente:" +Continentes.AMERICA.getHabitantes());
      
      System.out.println("Continente No. 5: "+Continentes.OCEANIA);
      System.out.println("No. de paises en el 5to. continente: "+Continentes.OCEANIA.getPaises());
      System.out.println("No. de habitantes en el 5to.continente:" +Continentes.OCEANIA.getHabitantes());
    } 
    private static void indicarDiaSemana( Dias dias){
        switch (dias){
            case lunes:
                System.out.println("Primer dia de la semana");
                break;
            case martes:
                System.out.println("segundo dia de la semana");
                break;
            case miercoles:
                System.out.println("tercer dia de la semana");
                break;
            case jueves:
                System.out.println("cuarto dia de la semana");
                break;
            case viernes:
                System.out.println(" quinto dia de la semana");
                break;
            case sábado:
                System.out.println("sexto dia de la semana");
                break;
            case Domingo:
                System.out.println("septimo dia de la semana");
                break;
            
                
                       
            
        }
    }
}
