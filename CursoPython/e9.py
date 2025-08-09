nombre="developer"
#   0   1   2   3   4
lista=["admin", nombre,5,5,2,"hacker"]
print(lista)


print(lista[0])
print(lista[2])
print("imprimiendo lista con el while")
i=0
while i <len(lista):
    print(lista[i])
    i+=1


print("imprimiendo lista con el for")
for valor in lista:
    print("valor de listas: ",valor)

def buscarIndexPorId(lista,id):
    index=0
    i=0
    while i <len(roles):
        if role [i]["id"]==2:
         index=i
        i=len(lista)
    i+=1
    return

role={
    "id":1,
    "nombre":"admin"
}

roles=[role]
print("valor de la lista con diccionario antes de modificar: ")
print(roles)
roles[0]["id"]=5
roles[0]["nombre"]="developer"
roles[0]={
   "id":1,
   "nombre":"ejemplo entero"
}
print("valor de la lista con diccionario despues de modificar: ")
print(roles)


#Agregar un nuevo elemento a la lista

roles.append(
    {
        "id":len(roles)+1,
        "nombre":"director"
    }
)
role=role.copy()
role["id"]=len(roles)+1
role["nombre"]="mago"

#agregar un nuevo elemento a la lista

roles.append(
    role
)
print("valor de la lista con diccionario despues de appened: ")
print(roles)


#buscar

index=buscarIndexPorId(roles,2)

#eliminar
roles.remove(roles[index])
print("Deberia eliminar al director")
print(roles)

