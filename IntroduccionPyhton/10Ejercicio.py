objetivo = int(input("Por favor, introduce cuántos números quieres introducir: "))
nums = []
cont = 0
while cont < objetivo:
    numeros = int(input("Escribe un numero: "))
    nums.append(numeros)
    cont += 1
else: 
    print("Estos son los números que has introducido ", nums)