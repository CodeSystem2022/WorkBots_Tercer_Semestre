package ar.com.system2023.mundopc;

public class Dispositivoentrada {
    private String tipoEntrada;
    private String marca;
    
public Dispositivoentrada(String tipoEntrada, String marca){
  this.tipoEntrada =tipoEntrada;
  this.marca=marca;
}

public String getTipoEntrada(){
    return tipoEntrada;
}

public void SetTipoEntrada (String TipoEntrada){
   this.tipoEntrada =tipoEntrada;
}
 public String getMarca(){
   return this.marca;  
 }
 
 public void setMarca (String marca){
     this.marca =marca;
 }

    @Override
    public String toString() {
        return "Dispositivoentrada{" + "tipoEntrada=" + tipoEntrada + ", marca=" + marca + '}';
    }
 
 
}
