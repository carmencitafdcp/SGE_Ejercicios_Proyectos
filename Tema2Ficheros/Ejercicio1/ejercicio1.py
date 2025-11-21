cont = 0

f = open('Tema2Ficheros/Ejercicio1/entrada.txt', 'r')
lineas = f.readlines()
f.close()

for linea in lineas:
    if linea.strip():
        cont += 1

print("Número de líneas escritas:", cont)
