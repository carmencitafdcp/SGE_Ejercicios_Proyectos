cantidad = int(input("¿Cuántos números quieres introducir? ")) 
nums = []
    
def mensaje(nums, cantidad):
    for n in range(cantidad):
        numero = int(input("Di un número: "))
        nums.append(numero)
        if n > 0 and numero <= nums[n-1]:
            print(f"El número {numero} es menor que el anterior.")


mensaje(cantidad)


    





