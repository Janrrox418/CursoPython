class Estudiante:
    def __init__(self, nombre, apellido, cedula, fecha_nac, grupo, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.fecha_nac = fecha_nac
        self.grupo = grupo
        self.telefono = telefono
        self.notas = []  

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def calcular_promedio(self):
        if not self.notas:
            return 0 
        return sum(self.notas) / len(self.notas)
    
    def mostrar_promedio_final(self):
        promedio = self.calcular_promedio()
        print(f"El promedio final de {self.nombre} {self.apellido} es: {promedio:.2f}")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido}, Cedula: {self.cedula}") 