import requests

#Pokemons desde el numero 1 al 1302
numero = 151
url_ejercicio = f"https://pokeapi.co/api/v2/pokemon/{numero}"

url = "https://pokeapi.co/api/v2/pokemon"

response = requests.get(url_ejercicio)
if response.status_code == 200:
    data = response.json()
    print(data["name"])
else:
    print(f"Error: {response.status_code}")

numeros = 3.5
redondeado = round(numeros)
print(redondeado)