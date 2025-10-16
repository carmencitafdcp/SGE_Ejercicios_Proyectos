objetivo = int(input("Por favor, introduce cuántos caracteres quieres escribir: "))
palabra = []
cont = 0
while cont < objetivo:
    carac = input("Escribe un carácter: ")
    palabra.append(carac[0])
    cont += 1
print ("Esta palabra es la que has introducido: ", palabra)



