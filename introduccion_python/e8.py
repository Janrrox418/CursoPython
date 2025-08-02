#funciones python



#funcion sin parametro y sin retorno
def bienvenida():
    nombre=input("Hola ¿Como te llamas?:  ")
    print(f"Bienvenido al proyecto {nombre}")



#Lllamado de una funcion o ejecucion
bienvenida()

#funcion con parametros y sin retorno
def bienvenidaPorNombre(nombre):
    print(f"Bienvenido al proyecto{nombre}")

#funcion sin parametros con retorno un string
def leernombre():
    nombre=input("Ingrese el nombre:  ")
    return nombre

name=leernombre()
bienvenidaPorNombre(name)
usuario=leernombre()
bienvenidaPorNombre(usuario)

#funcion con parametro pero sin retorno de datos
def suma(a,b):
    print(f"La suma es:  {float(a)+float(b)}")
suma(5,13)

#funcion con parametro con retorno de datos
def sumaconRetorno(a,b):
    return float(a)+float(b)


#funcion sin parametros con retorno un float
def leernumeroReal():
    numero=float(input("Ingrese el numero:  "))
    return numero
def leernumeroEntero():
    numero=int(input("Ingrese el numero entero:  "))
    return numero



suma(5,13)
numeroa=leernumeroReal()
numerob=leernumeroReal()
resultado=sumaconRetorno(numeroa,numerob)
print(f"El resultado es: {resultado}")
resultado=sumaconRetorno(5,13)
print(f"La suma de los numeros es: {resultado}")

#Funcion recursiva
def factorial(numero):
    if numero<0:
        return None
    elif numero ==0:
        return 1
    else:
        return numero*factorial(numero-1)
numero = leernumeroEntero()
calculo = factorial(numero)
if calculo != None:
    print(f"El factorial de {numero} es: {calculo}")
else:
    print(f"El factorial de un numero negativo no existe, numero ingresado: {numero}")