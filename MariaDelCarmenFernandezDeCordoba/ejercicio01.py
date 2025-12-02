num = int(input("Introduce cualquier número: "))
cantidad = int(input("¿Cuántos números quieres introducir? "))
lista_nums = []
lista_mayores = []
i = 0
maximo = 0

while i < cantidad:
    numeros = int(input("Escribe un número: "))
    lista_nums.append(numeros)
    i += 1

def numsMayores(num, lista_nums):
    lista = []
    for n in lista_nums:
        if n > num:
            lista.append(n)
    return lista

lista_mayores = numsMayores(num, lista_nums)

print(f"Había {len(lista_mayores)} números mayores que el tuyo.")
print(f"Y estos son dichos números: {lista_mayores}")
    
