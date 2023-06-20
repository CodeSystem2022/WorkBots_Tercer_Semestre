class Cliente extends persona {
    static contadorC = 0;

    constructor(nombre, apellido, edad, fechaRegistro) {
        super(nombre, apellido, edad);
        this._idCliente = ++Cliente.contadorC;
        this._fechaReg = fechaRegistro;
    }

    get idCliente() {
        return this._idCliente;
    }

    get fechaRegistro() {
        return this._fechaReg;
    }

    set fechaRegistro(fecha) {
        this._fechaReg = fecha;
    }

    toString() {
        return `${super.toString()} 
        ${this._idCliente}
        ${this._fechaRegistro}`;
    }
}