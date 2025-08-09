class Sistema:

    def __init__(self,mensaje,nombre):
        self._mensaje=mensaje
        self._nombre=nombre

    def bienvenida(self):
        print(f"{self._mensaje}: {self._nombre}")


    def leerNumeroEnteroPersonalizado(self,mensaje):
        numero=int(input(f"{mensaje}"))
        return numero
    
    def leerNumeroFloatPersonalizado(self,mensaje):
        numero=float(input(f"{mensaje}"))
        return numero
    
    def imprimirMensajePersonalizado(self,mensaje):
        print(mensaje)

    
    def leerTextoPersonalizado(self, mensaje):
     texto = input(mensaje)
     return texto
        