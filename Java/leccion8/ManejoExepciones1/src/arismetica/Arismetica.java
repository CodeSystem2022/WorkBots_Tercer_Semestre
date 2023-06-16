
package arismetica;

import excepciones.OperacionExcepcion;


public class Arismetica {
    public static int division(int numerador, int denominador) {   
    
        if(denominador == 0) {
            throw new OperacionExcepcion("División entre cero");            
        }
        return numerador / denominador;      
    }    
}
