#funcion sin parametros con retorno un float
def leernumeroEntero(mensaje):
    num1=int(input(f"{mensaje}: "))
    return num1
def leernumeroEntero(mensaje):
    num2=int(input(f"{mensaje}: "))
    return num2

#funcion sin parametros con retorno un string
def leerStringPersonalizado(mensaje):
    nombre=input(f"{mensaje}: ")
    return nombre

def valorAbsoluto(numero):
           calculo = 0.0
if valorAbsoluto >= 0:
            calculo=numero
else:
            calculo=numero*-1
print(f"El valor absoluto del numero: {numero} es {calculo}")


            
   








print("Bienvenido al Sistema")
print("Ingrese una de las siguientes opciones")
print("      1.saludo de bienvenida")
print("      2.calculadora")
print("      3.valor absoluto")
print("      4.promedio de notas")
print("      5.Inscripcion al Kinder")
print("      6.salir")
opcion=int(input("Ingrese una de las opciones: "))

while opcion !=6:
    if opcion ==1:
        print("      1.saludo de bienvenida")
        '''
           Saludo de Bienvenida con el nombre del usuario que solicita por teclado
        '''
        nombre=leerStringPersonalizado("¿Como te llamas?:  ")
        print(f"Bienvenido al Sistema {nombre}")
    elif opcion ==2:

        print("      2.calculadora")
        '''
           Crear una calculadora que
           Solicita dos numeros y pregunta que operacion quieren hacer
           s,r,m,d
        '''
       
        num1=leernumeroEntero("Ingresa un numero:  ")
        num2=leernumeroEntero("Ingresa un numero:  ")      
        operacion = input("¿Qué operación quieres hacer? (s, r, m, d): ")

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

    elif opcion ==3:
        print("      3.valor absoluto")
        '''
           Calculo del valor absoluto de un numero
        '''
        numero = float(input("Ingrese un numero: "))
        calculo = 0.0
        if numero >= 0:
            calculo=numero
        else:
            calculo=numero*-1
        print(f"El valor absoluto del numero: {numero} es {calculo}")

    elif opcion ==4:
        print("      4.promedio de notas")
        '''
           Realizar un algoritmo que calcule el promedio de rutas de una materia.
           En la materia se hicieron 3 evaluaciones, debe imprimir el boletin del estudiante
           con su nombre, nota e indicar si aprobo o reprobo, se aprueba con una nota mayor a 12 puntos,
           la nota es en esacala del 1 al 20
        '''
        nombre= input("Bienvenido por favor ingrese su nombre:  ")
        print(f"Bienvenido {nombre}")
        sumatoria=0.0 #acumulador
        for i in range(3): # 0 1 2
            nota=float(input(f"Ingrese la nota {i+1} : "))
            sumatoria+=nota
        promedio=sumatoria/3
        if promedio > 12:
            print(f"Felicidades {nombre} aprobaste!!! :) y tuviste un promedio de {promedio}")
        else:
            print(f"Lo sentimos {nombre} reprobaste:(    y tuviste un promedio de {promedio}")

    elif opcion == 5:
        print("      5.Inscripcion al Kinder")
        '''
           Inscripcion al kinder, si cumple la edad o si no la cumple
        '''
        edad=int(input("Ingrese la edad del estudiante: "))
        # para empezar a estudiar prescolar debe ser mayor o igual a 5 años, si cumple la condicion enviar un mensaje si no caso contrario
        if edad>=5:
            print("Sí puede estudiar en el Kinder.")
        else:
            print("No puede estudiar en el Kinder por la edad.")

    
    else: 
        print("Opción no válida. Por favor, ingrese un número entre 1 y 6.")

    
    print("\n")
    print("Ingrese una de las siguientes opciones")
    print("      1.saludo de bienvenida")
    print("      2.calculadora")
    print("      3.valor absoluto")
    print("      4.promedio de notas")
    print("      5.Inscripcion al Kinder")
    print("      6.salir")
    opcion=int(input("Ingrese una de las opciones: "))

print("¡Gracias por usar el sistema! Hasta luego.")