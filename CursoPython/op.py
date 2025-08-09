edad=int(input("Ingrese la edad del estudiante: "))
#para empezar a estudair prescolar debe ser mayor o igual a 5 años, si cumple la condicion enviar un mensaje si no caso contrario 
#edad>= 5 -> p
comparacion=edad >=5
print(f"Valor logico de:{comparacion} ")
if comparacion:
    print("Si puede estudiar")
else:
    print("No puede estudiar")

#division de dos numeros 
a=int(input("Ingrese el numero a: "))
b=int(input("Ingrese el numero b: "))
if b!=0:
    print(f"{a/b}")
if not b!=0:
    print("No se puede dividir entre 0")

    