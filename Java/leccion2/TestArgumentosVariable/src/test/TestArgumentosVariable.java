package test;

public class TestArgumentosVariable {
    public static void main(String[]args){
        imprimirNumeros(3,4,5);
        imprimirNumeros(1,2);
        Variosparámetros("Juan","perez",7,8,9);
        
    }
    
    private static void Variosparámetros(String nombre,String apellido,int...numeros){
           
        System.out.println("Nombres: "+nombre+",apellido: "+apellido);
        imprimirNumeros(numeros);
    }
    
    
    private static void imprimirNumeros(int...numeros){
        for(int i =0 ;i< numeros.length;++i){
            System.out.println("elementos:  "+ numeros[i]);
            
        }
    }

    private static void variosParámetros(String juan, int i, int i0, int i1) {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }
}
