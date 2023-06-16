class NumerosIgualesException (Exception): #Extiende la clase
    def __init__(self, mensaje):
        self.message = mensaje