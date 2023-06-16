
package paquete2;

public class Clase4 {
    private String atributoPrivate = "atributpo privado";
    
    private Clase4(){
        System.out.println("Constructor privado");
    }
    
    public Clase4(String argumento){
        this();
        System.out.println("Contructor publico");
    }
    
    //Método private
    private void metodoprivado(){
        System.out.println("Método privado");
    }

    public String getAtributoPrivate() {
        return atributoPrivate;
    }

    public void setAtributoPrivate(String atributoPrivate) {
        this.atributoPrivate = atributoPrivate;
    }
    
}
