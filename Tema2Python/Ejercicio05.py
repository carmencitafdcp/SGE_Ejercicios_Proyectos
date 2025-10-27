# 5. Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga
# cuántas veces aparece esa palabra en la lista.


palabras = []
maximo = 0
repetido = None

for i in range(5):
    palabra = input("Escribe una palabra: ")
    palabras.append(palabra)

print("Lista introducida:", palabras)

for palabra in palabras:
    count = palabras.count(palabra)
    if count > maximo:
        maximo = count
        repetido = palabra

if maximo > 1:
    print(f"La palabra '{repetido}' se repite {maximo} veces")
else:
    print("No hay palabras repetidas en la lista")
    