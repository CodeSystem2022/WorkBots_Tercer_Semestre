package paquete1;

public class Clase1 {
    public String atributoPublic = "Valor atributo public";
    protected String atributoProtected = "Valor atributo private";
    
    public Clase1(){
        System.out.println("Constructor public");
    }
    
    protected Clase1(String atributoPublic){
        System.out.println("Constructor protected");
    }
    
    public void metodoPublico(){
        System.out.println("Método public");
    }
    
    protected void motodoProtected(){
        System.out.println("Método protected");
    }
}
    

