num = int(input("Introduce cualquier número: "))
cantidad = int(input("¿Cuántos números quieres introducir? "))
lista_nums = []
i = 0
maximo = 0
contador = 0

while i < cantidad:
    numeros = int(input("Escribe un número: "))
    lista_nums.append(numeros)
    i += 1

def numsMayores(num, lista_nums):
    contador_local = 0
    for n in lista_nums:
        if n > num:
            contador_local += 1
    return contador_local

contador = numsMayores(num, lista_nums)

print(f"Había {contador} números mayores que el tuyo.")
    
