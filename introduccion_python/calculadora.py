'''
Solicita dos numeros y pregunta que operacion quieren hacer 
s,r,m,d
'''
numero1=int(input("Ingrese un numero: "))
numero2=int(input("Ingrese un numero: "))

print("Operaciones que se pueden realizar:")
print("s")
print("r")
print("m")
print("d")

operacion=(input("Escriba la operacion que desea hacer (s/r/m/d): "))

if operacion == 's':
    resultado=numero1+numero2
    print(f"El resultado es {resultado}")
    if operacion == 'r':
        resultado=numero1-numero2
        print(f"El resultado es {resultado}")
        if operacion == 'm':
            resultado=numero1*numero2
            print(f"El resultado es {resultado}")
            if operacion == 'd':
                resultado=numero1/numero2
                print(f"El resultado es {resultado}")



   






