print("Bienvenido a las respuestas del examen")
print("Escriba alguno de los siguientes numeros")
print("      1.Respuesta de la 2.3")
print("      2.Respuesta de la 3.3")
print("      3.Respuesta de la 2.4")
print("      4.Salir")

opcion=int(input("Ingrese una de las opciones: "))

while opcion != 4:
  if opcion == 1:
      print("      1.Respuesta de la 2.3")

      #Respuesta 2.3
      def doble_numero(numero):
        return numero * 2

      numero = 5
      resultado = doble_numero(numero)
      print(f"El doble de {numero} es {resultado}")

  elif opcion == 2:
     print("      2.Respuesta de la 3.3")
    
          #Respuesta de la 4.3
     
     ciudades =["Barquisimeto", "Caracas", "Margarita"]

     print(ciudades)

     colores = {"azul", "verde", "rojo"}

     print(colores)

     informacion = {
      "nombre": "Luis",
       "edad": 22
            }

     print(informacion)
     '''
      una variable global se define fuera de cualquier función y puede ser accedida desde cualquier parte del programa, 
       mientras que una variable local se define dentro de una función y solo puede ser accedida dentro de esa función. 
        '''
  elif opcion == 3:
    print("3.Respuesta de la 2.4")

    # Respuesta de la 2.4
    var_global = 10

    def mi_funcion():
        var_local = 5
        print("Dentro de la función:")
        print("Variable global:", var_global)
        print("Variable local:", var_local)

    mi_funcion()

    print("\nFuera de la función:")
    print("Variable global:", var_global)
    


else: 
        print("Opción no válida. Por favor, ingrese un número entre 1 y 4.")
        print("\n")
        print("Escriba alguno de los siguientes numeros")
        print("      1.Respuesta de la 2.3")
        print("      2.Respuesta de la 3.3")
        print("      3.Respuesta de la 2.4")
        print("      4.Salir")

print("¡Gracias por usar el sistema! Hasta luego.")