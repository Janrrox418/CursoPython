edad=int(input("Ingrese la edad del estudiante: "))
#para empezar a estudair prescolar debe ser mayor o igual a 5 años, si cumple la condicion enviar un mensaje si no caso contrario 
#edad>= 5 -> p
comparacion=edad >=5
if comparacion:
    print("Si puede estudiar")
else:
    print("No puede estudiar")
    