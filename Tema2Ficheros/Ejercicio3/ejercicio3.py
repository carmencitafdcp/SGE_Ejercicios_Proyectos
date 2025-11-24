contenido = ""

f = open("Tema2Ficheros/Ejercicio3/origen.txt")
contenido = f.read()   
f.close()              

copia = open("Tema2Ficheros/Ejercicio3/copia.txt", "w")
copia.write(contenido)   
copia.close()               

print("Se ha realizado la copia correctamente.")
