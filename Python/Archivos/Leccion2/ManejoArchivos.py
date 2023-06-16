class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print('Objetemos el recurso'.center(50,'-'))
        self.nombre = open(self.nombre,'r',encoding='utf8') #Encapsulamos el codigo del metodo
        return self.nombre

    def __exit__(self, tipo_exception, valor_exception, traza_error):
        #self.tipo_exception = tipo_exception
        #self.valor_exception = valor_exception
        #self.traza_error = traza_error
        print('cerramos el recurso'.center(50,'-'))
        if self.nombre:
            self.nombre.close() #cerramos el archivo
