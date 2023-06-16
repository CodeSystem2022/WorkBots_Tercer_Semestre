package test;

import domain.Persona;

public class testForEach {
    public static void main(String[] args){
        int edades[] = {5, 6, 8, 9};
        for (int edad: edades) {
            System.out.println("edad = "+ edad);
        }
        
        Persona personas[] = {new Persona ("Juan"), new Persona("Carla"), new Persona ("Beatriz")};
        //ForEach
        for(Persona persona :personas){
            System.out.println("personas ="+persona);
            
        }
    }
}
