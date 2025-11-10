palabras = ['hola', 'verde', 'árbol', 'gominolas', 'chocolate', 'ardilla', 'flores']
print(f"Esta es la lista original {palabras}")

palabraVieja = input("Palabra a sustituir: ")
palabraNueva = input("Palabra nueva: ")

for i in range (len(palabras)):
    if palabras[i] == palabraVieja:
        palabras[i] = palabraNueva

print(f"Esta es ahora la lista modificada: {palabras}")