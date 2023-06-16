let x = 10; // Variable de tipo primitiva
console.log(x.length)


//Objeto -- De esta manera nos permite acceder a mas opciones a la hora de ser llamada 
let persona = {
    nombre: 'Facundo',
    segundoNombre: 'Leonel',
    apellido: 'Cano',
    edad: 20,
    altura: 1.78,
    idioma : 'español',
    email: 'facundocano79@gmail.com',
    get lang(){// el metodo {lang} hace referencia a los idiomas
        return this.idioma.toUpperCase(); //Convierte las minusculas a mayusculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function(){ // metodo o funcion en JavaScript
        return this.nombre+' '+this.segundoNombre+' '+this.apellido;
    },
    get nombreEdad(){
        return 'El Nombre es: '+this.nombre+', Edad: '+this.edad;
    }
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.edad);
console.log(persona.altura);
console.log(persona.email);
// o de esta manera
console.log(persona.nombreCompleto());


// Diferentes formas de crear objetos

let persona2 = new Object(); // Debe Crear un nuevo objeto en memoria
persona2.nombre = 'Santiago';
persona2.direccion = 'Br Guemeez';
persona2.telefono = '2414251525';
console.log(persona2.telefono);

//Accedemos como si fuera un Arreglo
console.log(persona['apellido']);

//for in
// como acceder a la propiedad y luego a su valor
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}


//Agregar y eliminar propiedades de un Objeto
persona.apellidos = 'Perez';// Cambiamos dinamicamnete un valor del objeto
delete persona.apellidos
console.log(persona);


// Distintas Formas de Imprimir un Objeto
// Numero 1: la mas sencilla: concatenar cada valor de cada propiedad
console.log('Distintas formas de imprimir un Objeto = Forma 1')
console.log(persona.nombre+' '+persona.apellido);

//Numero 2: A traves de un Ciclo for in
console.log('Distintas formas de imprimir un Objeto = Forma 2');
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

//Numero 3: La funcion Objet.values()
console.log('Distintas formas de imprimir un Objeto = Forma 3');
let personaArray = Object.values(persona);
console.log(personaArray);

//Numero 4: Utilizamos el metodo JSON.stringify
console.log('Distintas formas de imprimir un Objeto = Forma 4');
let personaString = JSON.stringify(persona);
console.log(personaString);

console.log('Comenzamos a utilizar el metodo {get}')
console.log(persona.nombreEdad)

console.log('Comenzamos con el metodo {get y set} para idiomas')
persona.lang = 'Ingles'
console.log(persona.lang);


//Contructor

function Persona3(nombre, apellido, email){// Constructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    //Agregamos metodos al contructor
    this.nombreCompleto = function(){
        return this.nombre+' '+this.apellido
    }
}
let padre = new Persona3('Leo','Lopez','lopezln@gmail.com')
padre.nombre = 'Luis';//se puede modificar
console.log(padre);
console.log(padre.nombreCompleto());//Utilizamos la funcion

let madre = new Persona3('Laura','Contreras','laucontre@gmail.com')
console.log(madre);
console.log(madre.nombreCompleto());

//Diferentes formas de crear objetos

// Forma Obejto 1
let miObjeto = new Object(); //Opcion Formal

// Forma Objeto 2
let miObjeto2 = {};//Esta opcion es breve y recomendada

// Caso String 1
let miString = new String('Hola');//Opcion Formal

// Caso String 2
let miString2 = 'Hola';//Opcion Breve y Recomedada

// Caso Numero 1
let numero = new Number(1); //Opcion Formal

// Caso Numero 2
let numero2 = 5; //Opcion Breve y Recomendada

// Caso Boolean 1
let miBooleano = new Boolean(false);//Opcion Formal

// Caso Boolean 2
let miBooleano2 = false;//Opcion Breve y Recomendada

// Caso Arreglos 1
let miArreglo = new Array();//Opcion Formal

// Caso Arreglo 2
let miArreglo2 = [];//Opcion Breve y Recomendada

// Caso Funcion 1
let miFuncion = new function(){}; //Todo despues del new es considerado objeto

//Caso Funcion 2
let miFuncion2 = function(){}; //Notacion de la forma simplificada

// Uso de Prototype
Persona3.prototype.telefono ='2376421478';
console.log(padre);
console.log(madre.telefono);
madre.telefono = '1343435523';
console.log(madre);

// Uso del Call
let Persona4 = {
    nombre : 'Juan',
    apellido : 'Alvarez',
    nombreCompleto2: function(titulo, telefono){
        return titulo+' : '+ this.nombre +' '+ this.apellido+', Telefono :'+telefono
    }
}


let Persona5 = {
    nombre : 'Juliana',
    apellido : 'Dominguez'
}

console.log(Persona4.nombreCompleto2('Tecnicatura en Programacion', '2874362416842'));

// Usamos elmetodo (call) para llamar a una funcion que necesitamos en otro lugar
console.log(Persona4.nombreCompleto2.call(Persona5, 'Ingeniera', '765476476685'));


// Metodo Apply
// El metodo (apply) necesita un arreglo aparte para poder funcionar 
let arreglo =['Licenciada','3452524624'];
console.log(Persona4.nombreCompleto2.apply(Persona5, arreglo));