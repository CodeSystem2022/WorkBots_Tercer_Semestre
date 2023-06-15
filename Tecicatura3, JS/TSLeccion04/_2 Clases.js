// let persona3 = new Persona('Carla', 'Ponse'); No se puede porque aun no esta definida la calse Persona  

class Persona{// Clase Padre
    // Atribuito statico
    static contadorPersonas = 0;// Atribuito statico

    static get MAX_OBJ(){// Este metodo simula una constante que limita la creacion de objetos en la calse Padre
        return 5;
    }
    email = 'Valor default emailing';// Atribuito no statico

    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
        
        if(Persona.contadorPersonas < Persona.MAX_OBJ){
            this.idPersona = ++Persona.contadorPersonas; 
        }
        else{
            console.log('Se ha superado el maximo de objetos permitidos');
        }

        //this.contadorObjetosPersona;// esto no se debe hacer porque apunta a la referencia de un objeto 
        
        //Persona.contadorPersonas++;// hacemos que sume con el (++)
        
        //console.log('Se incrementa el contador:'+Persona.contadorObjetosPersona);
    }

    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }

    get apellido(){
        return this._apellido;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }

    nombreCompleto(){
        return this.idPersona+' '+this._nombre+' '+this._apellido
    }

    // Sobreescribiendo el metodo de la calse Padre (Objet )
    toString(){  // Regresa un String
        // Se aplica el polimorfismo que significa = multiples formas en tiempo de ejecucion
        // El metodo que se ejecuta depende si es una referencia de tipo padre o hija 
        return this.nombreCompleto();
    }

    static saludar(){
        console.log('Saludos desde este metodo static');
    }

    static saludar2(persona){
        console.log(persona.nombre+' '+persona.apellido);
    }
}

// Usamos(extends) para unir la Clase Padre(Persona) con la Clase Hija(Empleado)
class Empleado extends Persona{
    constructor(nombre, apellido, departamento){
        super(nombre, apellido);// Se utiliza (super) para llamar a los atributos de la clase Padre
        this._departamento = departamento;
    }
    
    get departamento(){
        return this._departamento;
    }
    
    set departamento(departamento){
        return this._departamento = departamento
    }

    // Sobreescribir: es modificar el comportamiento de algun metodo de la calse Padre(Persona)
    nombreCompleto(){
        return super.nombreCompleto()+', '+this._departamento;// Utilizamos (super) para no repetir el codigo [this._nombre + this._apellido] que esta en la clase Padre(Persona)
    }
}
// Caso Nombre persona1
let persona1 = new Persona('Martin', 'Perez');
console.log(persona1.nombre);
persona1.nombre = 'Facundo';
console.log(persona1.nombre)

// Caso Apellido persona1
console.log(persona1.apellido);
persona1.apellido = 'Cano';
console.log(persona1.apellido);
console.log(persona1);

//----------------------------------------------------------------

// Caso Nombre persona2
let persona2 = new Persona('Lucas', 'Rojas');
console.log(persona2.nombre);
persona2.nombre ='Leonel';
console.log(persona2.nombre);

// Caso Apellido persona2
console.log(persona2.apellido);
persona2.apellido = 'Romero'
console.log(persona2.apellido);
console.log(persona2);

// Caso Clase Hija
let empleado1 = new Empleado('Leo','Ferro', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombreCompleto());
