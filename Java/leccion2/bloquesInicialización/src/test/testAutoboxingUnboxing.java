package test;
public class testAutoboxingUnboxing {
    public static void main (String[] args){
        //clases envolventes o Wrapper
        /*
        clase envolvente de tipos primitivos
        int = la clases envolvente es Integer
        */
        int enteroPrim =10; //Tipo primitivo
        Integer entero = 10;// Tipo object con la clases Integer
        System.out.println("entero = "+entero.byteValue());//Autoboxing
        
        int entero2 =entero; //Unboxing
        System.out.println("entero2  ="+entero2);
        
        
        
    }
}
