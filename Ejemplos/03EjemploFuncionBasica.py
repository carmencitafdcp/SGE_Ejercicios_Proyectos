cantidad = int(input("¿Cuántos números deseas introducir?  "))
nums = []
i = 0

while i < cantidad:
    numeros = int(input("Introduce un número: "))
    nums.append(numeros)
    i += 1

def ordenarYmultiplicar(nums):
    total = 1
    for n in nums:
        total = total * n
    print(sorted(nums))
    print(f"El total de multiplicar es: {total}")

print(ordenarYmultiplicar(nums))

