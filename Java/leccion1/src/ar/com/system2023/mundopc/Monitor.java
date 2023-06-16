package ar.com.system2023.mundopc;

public class Monitor {
    private final int IdMonitor;
    private String marca;
    private double tamanio;
    private static int contadorMonitores;
    private int idMonitor;
    
    private Monitor(){
        this.IdMonitor = ++Monitor.contadorMonitores;
        
    }
    public Monitor(String marca, double tamanio){
        this(); //llamado al constructor vacio
        this.marca =marca;
        this.tamanio = tamanio;
        
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public double getTamanio() {
        return tamanio;
    }

    public void setTamanio(double tamanio) {
        this.tamanio = tamanio;
    }
    //ingresamos manuelamente el getMonitor
     public int getidMonitor(){
       return this.idMonitor;
    }    

    @Override
    public String toString() {
        return "Monitor{" + "IdMonitor=" + IdMonitor + ", marca=" + marca + ", tamanio=" + tamanio + '}';
    }
    
}
