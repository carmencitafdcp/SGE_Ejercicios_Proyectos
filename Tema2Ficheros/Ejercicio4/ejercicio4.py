numero = 1
lineaNum = ""

f = open("Tema2Ficheros/Ejercicio4/texto.txt")

n = open("Tema2Ficheros/Ejercicio4/numerado.txt", "w")

for linea in f:
    lineaNum = str(numero) + ": " + linea
    n.write(lineaNum)
    numero += 1

f.close()
n.close()

print("Texto numerado correctamente!")
