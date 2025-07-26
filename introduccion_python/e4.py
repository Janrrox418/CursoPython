'''
    Realizar un algoritmo que calcule el promedio de rutas de una materia.
    En la materia se hicieron 3 evaluaciones, debe imprimir el boletin del estudiante
    con su nombre, nota e indicar si aprobo o reprobo, se aprueba con una nota mayor a 12 puntos,
    la nota es en esacala del 1 al 20
'''

nombre = input("Bienvenido por favor ingrese su nombre:  ")
print(f"Bienvenido {nombre}")
nota1 = float(input("Por favor ingrese sus nota1: "))
nota2 = float(input("Por favor ingrese sus nota2: "))
nota3 = float(input("Por favor ingrese sus nota3: "))


promedio =(nota1+nota2+nota3)/3

if promedio > 12:
    print(f"Felicidades {nombre} aprobaste!!! :) y tuviste un promedio de {promedio}")
else:
    print(f"Lo sentimos {nombre} reprobaste:(  y tuviste un promedio de {promedio}")

    
