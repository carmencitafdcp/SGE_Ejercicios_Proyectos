f = open('temps.txt', 'r') # Función para abrir ficheros
contenido = f.read()
print(contenido)

f.seek(0) #Volvemos al inicio deel fichero.
linea1 = f.readline()
print("Primera línea del fichero: ")
print(linea1)

#Bucle para ir leyendo línea a línea
print("Leyendo línea a línea ccon un bucle: ")
f.seek(0)
for linea in f:
    print(linea, end='')

#Otra forma de ir leyendo línea a línea
f.seek(0)
lineas = f.readlines()
print("\nContenido del fichero leído con readlines(): ")
for linea in lineas:
    print(linea, end = '')
f.close()