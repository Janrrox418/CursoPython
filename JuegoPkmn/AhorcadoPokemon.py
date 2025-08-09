import requests
import random


def obtener_pokemon():
    #Usamos id aleatorio para obtener un Pokémon entre 1 y 1302
    id_aleatorio = random.randint(1, 1302)
    url = f"https://pokeapi.co/api/v2/pokemon/{id_aleatorio}/"
    respuesta = requests.get(url)


    if respuesta.status_code == 200:
        datos_pokemon = respuesta.json()
        nombre_pokemon = datos_pokemon['name']
        return nombre_pokemon.upper() # esto es paara que el nombre del Pokémon esté en mayúsculas
    else:
        return None
    
#Usaremos una lista para colocar las etapas del dibujo del ahorcado
etapas_ahorcado = [
    """
     -----          
     |   |          
     |   O          
     |  /|\\
     |  / \\
     |
    """,
    """
     -----
     |   |
     |   O
     |  /|\\
     |  /
     |
    """,
    """
     -----
     |   |
     |   O
     |  /|
     |
     |
    """,
    """
     -----
     |   |
     |   O
     |   |
     |
     |
    """,
    """
     -----
     |   |
     |   O
     |
     |
     |
    """,
    """
     -----
     |   |
     |
     |
     |
     |
    """,
    """
     -----
     
     
     
     
     
    """,
]
    

def jugar_ahorcado(palabra):
    letras_adivinadas = set()
    errores = 0
    intentos = len(etapas_ahorcado) - 1 # Número de intentos permitidos

    print("\n¡Bienvenido al juego del Ahorcado Pokémon!")
    print("Adivina el nombre del Pokémon. Tienes", intentos, "intentos.\n")

    while errores < intentos:
        palabra_oculta = ''.join([letra if letra in letras_adivinadas else '_' for letra in palabra])
        print(etapas_ahorcado[errores])
        print(f"\nPalabra: {palabra_oculta}")
        print(f"Intentos restantes: {intentos - errores}\n")

        if '_' not in palabra_oculta: 
            print(f"¡Felicidades! Has adivinado el Pokémon: {palabra}.")
            break
 
        intento = input("Ingresa una letra: ").upper()

        if len(intento) != 1 or not intento.isalpha():
            print("Por favor, ingresa solo una letra.")
            continue

        if intento in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
        elif intento in palabra:
            print(f"correcto! La letra '{intento}' está en el nombre del pokemon.")
            letras_adivinadas.add(intento)

        
        else:
            print(f"\nError! La letra '{intento}' no está en el nombre del pokemon.")
            letras_adivinadas.add(intento)
            errores += 1


    else:
     print(etapas_ahorcado[-1])
     print(f"\nPerdiste. El Pokémon era: {palabra}")


def main():
 while True:
    pokemon = obtener_pokemon()
    if pokemon:
        jugar_ahorcado(pokemon)
    else:
        print("Error al obtener el Pokémon. Inténtalo de nuevo más tarde.")

    jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ").strip().lower()
    if jugar_nuevamente != 's':
        print("¡Gracias por jugar! Hasta luego.")
        break

if __name__ == "__main__":
    main()

