# Función sin parámetros con retorno de un entero
def leerNumeroEntero(mensaje):
    numero = int(input(f"{mensaje}: "))
    return numero

# Función sin parámetros con retorno de un string
def leerStringPersonalizado(mensaje):
    texto = input(f"{mensaje}: ")
    return texto

# Función con parámetro y retorno de un float (valor absoluto)
def valorAbsoluto(numero):
    if numero >= 0:
        return numero
    else:
        return numero * -1


videojuegos = ["The Legend of Zelda", "Minecraft", "GTA V", "Fortnite"]


print("Bienvenido al Sistema")

opcion = 0
while opcion != 6:
    print("\nIngrese una de las siguientes opciones")
    print("      1. Saludo de bienvenida")
    print("      2. Calculadora")
    print("      3. Valor absoluto")
    print("      4. Promedio de notas")
    print("      5. Inscripción al Kinder")
    print("      6. Gestión de Videojuegos")
    print("      7. Salir")  
    
    opcion = int(input("Ingrese una de las opciones: "))

    if opcion == 1:
        print("\n--- Saludo de Bienvenida ---")
        nombre = leerStringPersonalizado("¿Cómo te llamas?")
        print(f"Bienvenido al Sistema, {nombre}")

    elif opcion == 2:
        print("\n--- Calculadora ---")
        num1 = leerNumeroEntero("Ingresa un número")
        num2 = leerNumeroEntero("Ingresa otro número")      
        operacion = input("¿Qué operación quieres hacer? (s = suma, r = resta, m = multiplicación, d = división): ")

        if operacion == 's':
            print(f"La suma es: {num1 + num2}")
        elif operacion == 'r':
            print(f"La resta es: {num1 - num2}")
        elif operacion == 'm':
            print(f"La multiplicación es: {num1 * num2}")
        elif operacion == 'd':
            if num2 != 0:
                print(f"La división es: {num1 / num2}")
            else:
                print("No se puede dividir por cero.")
        else:
            print("Operación no válida.")

    elif opcion == 3:
        print("\n--- Valor absoluto ---")
        numero = float(input("Ingrese un número: "))
        resultado = valorAbsoluto(numero)
        print(f"El valor absoluto del número {numero} es {resultado}")

    elif opcion == 4:
        print("\n--- Promedio de notas ---")
        nombre = leerStringPersonalizado("Bienvenido, por favor ingrese su nombre")
        sumatoria = 0.0
        for i in range(3):
            nota = float(input(f"Ingrese la nota {i+1} (1-20): "))
            sumatoria += nota
        promedio = sumatoria / 3
        if promedio > 12:
            print(f"Felicidades {nombre}, aprobaste con un promedio de {promedio:.2f}")
        else:
            print(f"Lo sentimos {nombre}, reprobaste con un promedio de {promedio:.2f}")

    elif opcion == 5:
        print("\n--- Inscripción al Kinder ---")
        edad = leerNumeroEntero("Ingrese la edad del estudiante")
        if edad >= 5:
            print("Sí puede estudiar en el Kinder.")
        else:
            print("No puede estudiar en el Kinder por la edad.")

    elif opcion == 6:
        sub_opcion = 0
        while sub_opcion != 5:
            print("\n--- Gestión de Videojuegos ---")
            print("1. Ver lista de videojuegos")
            print("2. Agregar un nuevo videojuego")
            print("3. Buscar un videojuego")
            print("4. Eliminar un videojuego")
            print("5. Volver al menú principal")
            
            sub_opcion = int(input("Seleccione una opción: "))

            if sub_opcion == 1:
                print("\nLista de videojuegos:")
                for i, juego in enumerate(videojuegos, start=1):
                    print(f"{i}. {juego}")

            elif sub_opcion == 2:
                nuevo_juego = leerStringPersonalizado("Ingrese el nombre del nuevo videojuego")
                videojuegos.append(nuevo_juego)
                print(f"'{nuevo_juego}' ha sido agregado a la lista.")

            elif sub_opcion == 3:
                buscar = leerStringPersonalizado("Ingrese el nombre del videojuego a buscar")
                if buscar in videojuegos:
                    print(f"'{buscar}' está en la lista.")
                else:
                    print(f"'{buscar}' no se encontró en la lista.")

            elif sub_opcion == 4:
                eliminar = leerStringPersonalizado("Ingrese el nombre del videojuego a eliminar")
                if eliminar in videojuegos:
                    videojuegos.remove(eliminar)
                    print(f"'{eliminar}' ha sido eliminado de la lista.")
                else:
                    print(f"'{eliminar}' no se encontró en la lista.")

            elif sub_opcion == 5:
                print("Regresando al menú principal...")
            else:
                print("Opción no válida en gestión de videojuegos.")

    elif opcion == 7:
        print("\n¡Gracias por usar el sistema! Hasta luego.")

    else:
        print("\nOpción no válida. Por favor, ingrese un número entre 1 y 7.")
