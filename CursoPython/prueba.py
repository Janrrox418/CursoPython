try:
    x = int("abc")
except ValueError:
    print("Error de conversion")
finally:
    print("Fin del programa")