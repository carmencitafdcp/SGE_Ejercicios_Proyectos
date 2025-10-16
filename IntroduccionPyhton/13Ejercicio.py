num = int(input("Escribe de qué número quieres conocer el factorial: "))
cont = 0
factorial = 1
while cont < num:
    cont+=1
    factorial *= cont
print("El factorial de tu número es: ", factorial)