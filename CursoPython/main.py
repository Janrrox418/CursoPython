# main.py

import clases.calculadora as cal
import clases.sistema as sis
import clases.estudiante as estud
import clases.universidad as univ # Importar la clase Universidad

nombre = input("Por favor ingrese su nombre: ")

sistema = sis.Sistema("¡Bienvenido al Sistema!", nombre)
universidad = univ.Universidad() # Crear una instancia de Universidad

opcion = -1
while opcion != 4: # Cambiar la condición del bucle a 4
    sistema.bienvenida()
    sistema.imprimirMensajePersonalizado("Ingrese una de las siguientes opciones:")
    sistema.imprimirMensajePersonalizado(" 1. Calculadora")
    sistema.imprimirMensajePersonalizado(" 2. Gestión de Estudiantes") # Nuevo menú para estudiantes
    sistema.imprimirMensajePersonalizado(" 3. Promedio Estudiante (Individual)")
    sistema.imprimirMensajePersonalizado(" 4. Salir")
    opcion = int(sistema.leerNumeroEnteroPersonalizado("Ingrese una de las opciones: "))

    if opcion == 1:
        sistema.imprimirMensajePersonalizado("Entrando en la calculadora")

        numero_a = sistema.leerNumeroFloatPersonalizado("Ingrese el número a: ")
        numero_b = sistema.leerNumeroFloatPersonalizado("Ingrese el número b: ")

        calculadora = cal.calculadora(numero_a, numero_b)

        sistema.imprimirMensajePersonalizado("--------------------------")
        sistema.imprimirMensajePersonalizado(f"La suma de {numero_a} + {numero_b} = {calculadora.sumar()}")
        sistema.imprimirMensajePersonalizado(f"La resta de {numero_a} - {numero_b} = {calculadora.restar()}")
        sistema.imprimirMensajePersonalizado(f"La multiplicación de {numero_a} * {numero_b} = {calculadora.multiplicar()}")
        if calculadora.dividir() is not None:
            sistema.imprimirMensajePersonalizado(f"La división de {numero_a} / {numero_b} = {calculadora.dividir()}")
            abs_a, abs_b = calculadora.valor_absoluto()
            sistema.imprimirMensajePersonalizado(f"El valor absoluto de {numero_a} es {abs_a}")
            sistema.imprimirMensajePersonalizado(f"El valor absoluto de {numero_b} es {abs_b}")

    elif opcion == 2:
        sistema.imprimirMensajePersonalizado("--- Gestión de Estudiantes ---")
        opcion_estudiante = -1
        while opcion_estudiante != 4:
            sistema.imprimirMensajePersonalizado("Opciones de estudiantes:")
            sistema.imprimirMensajePersonalizado(" 1. Agregar estudiante")
            sistema.imprimirMensajePersonalizado(" 2. Listar estudiantes")
            sistema.imprimirMensajePersonalizado(" 3. Eliminar estudiante")
            sistema.imprimirMensajePersonalizado(" 4. Volver al menú principal")
            opcion_estudiante = int(sistema.leerNumeroEnteroPersonalizado("Seleccione una opción: "))

            if opcion_estudiante == 1:
                nombre_estudiante = sistema.leerTextoPersonalizado("Ingrese el nombre del estudiante: ")
                apellido_estudiante = sistema.leerTextoPersonalizado("Ingrese el apellido del estudiante: ")
                cedula_estudiante = sistema.leerTextoPersonalizado("Ingrese la cédula del estudiante: ")
                fecha_nac_estudiante = sistema.leerTextoPersonalizado("Ingrese la fecha de nacimiento del estudiante: ")
                grupo_estudiante = sistema.leerTextoPersonalizado("Ingrese el grupo del estudiante: ")
                telefono_estudiante = sistema.leerTextoPersonalizado("Ingrese el telefono del estudiante: ")
                
                nuevo_estudiante = estud.Estudiante(nombre_estudiante, apellido_estudiante, cedula_estudiante, fecha_nac_estudiante, grupo_estudiante, telefono_estudiante)
                universidad.agregar_estudiante(nuevo_estudiante)

            elif opcion_estudiante == 2:
                universidad.listar_estudiante()
            
            elif opcion_estudiante == 3:
                cedula_a_eliminar = sistema.leerTextoPersonalizado("Ingrese la cédula del estudiante a eliminar: ")
                universidad.eliminar_estudiante(cedula_a_eliminar)

            elif opcion_estudiante == 4:
                sistema.imprimirMensajePersonalizado("Volviendo al menú principal.")

            else:
                sistema.imprimirMensajePersonalizado("Opción incorrecta. Intente de nuevo.")

    elif opcion == 3:
        sistema.imprimirMensajePersonalizado("--- Promedio Estudiante---")
        
        nombre_estudiante = sistema.leerTextoPersonalizado("Ingrese el nombre del estudiante: ")
        apellido_estudiante = sistema.leerTextoPersonalizado("Ingrese el apellido del estudiante: ")
        cedula_estudiante = sistema.leerTextoPersonalizado("Ingrese la cédula del estudiante: ")
        fecha_nac_estudiante = sistema.leerTextoPersonalizado("Ingrese la fecha de nacimiento del estudiante: ")
        grupo_estudiante = sistema.leerTextoPersonalizado("Ingrese el grupo del estudiante: ")
        telefono_estudiante = sistema.leerTextoPersonalizado("Ingrese el telefono del estudiante: ")

        estudiante = estud.Estudiante(nombre_estudiante, apellido_estudiante, cedula_estudiante, fecha_nac_estudiante, grupo_estudiante, telefono_estudiante)
        
        for i in range(3):
            nota = sistema.leerNumeroFloatPersonalizado(f"Ingrese la nota {i+1}: ")
            estudiante.agregar_nota(nota)
        
        estudiante.mostrar_promedio_final()

    elif opcion == 4:
        sistema.imprimirMensajePersonalizado("Saliendo del sistema")

    else:
        sistema.imprimirMensajePersonalizado("Opción incorrecta. Por favor, intente de nuevo.")