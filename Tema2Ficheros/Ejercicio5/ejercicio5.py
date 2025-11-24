lineasInvertidas = 0
f = open("Tema2Ficheros/Ejercicio5/datos.txt")

lineas = f.readlines()
f.close() 
lineasInvertidas = lineas[::-1]

Finvertido = open("Tema2Ficheros/Ejercicio5/invertido.txt", "w")

for linea in lineasInvertidas:
    Finvertido.write(linea + '\n')
Finvertido.close() 

print("Se han impreso las líneas invertidas correctamente.")
