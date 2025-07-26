#Calculo del valor absoluto de un numero 

numero = float(input("Ingrese un numero: "))
calculo = 0.0

if numero >= 0:
        calculo=numero
else:
        calculo=numero*-1

print(f"El valor absoluto del numero: {numero} es {calculo}")
