'''
Solicita dos numeros y pregunta que operacion quieren hacer 
s,r,m,d
'''
num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese un numero: "))

print("Operaciones que se pueden realizar:")
print("s")
print("r")
print("m")
print("d")

operacion=(input("Escriba la operacion que desea hacer (s/r/m/d): "))

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




   






