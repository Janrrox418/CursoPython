class Universidad:
  
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"Estudiante {estudiante.nombre} agregado exitosamente")

    def buscar_estudiante(self, cedula):
        for estudiante in self.estudiantes:
            if estudiante.cedula == cedula:
                return estudiante
            return None
    
    def eliminar_estudiante(self, cedula):
        estudiante_a_eliminar = self.buscar_estudiante(cedula)
        if estudiante_a_eliminar:
            self.estudiantes.remove(estudiante_a_eliminar)
            print(f"Estudiante con cedula {cedula} eliminado correctamente")
        else:
            print(f"Error: no existe estudiante con esa cedula")
            

    def listar_estudiante(self):
        if not self.estudiantes:
            print("No hay estudiantes registrados")
        else:
            print("-----Lista de estudiantes------")
            for estudiante in self.estudiantes:
                print("Nombre: {estudiante.nombre}, Apellido {estudiante.apellido}")
                print("------------------")
    
            

        
         







   





      

    
    
    
            

   