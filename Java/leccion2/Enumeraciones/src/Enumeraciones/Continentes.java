
package Enumeraciones;

public enum Continentes {
    AFRICA (53,"1.2 billones"),
    EUROPA (46, "1.4 billones"),
    ASIA (44, "1.3 billones"),
    AMERICA (34,"1.8 billones"),
    OCEANIA (14,"1.9 billones");
 
    
    private final int paises;
    private String habitantes;
    Continentes(int paises, String habitantes){
        this.paises=paises;
        this.habitantes = habitantes;
    }
    
    // Método Get
    public int getPaises(){
        return this.paises;
    }
    public String getHabitantes(){
               return this.habitantes;

    }
       
}
