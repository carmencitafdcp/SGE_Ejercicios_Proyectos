sorpresa = int(input("introduce un número entre 0 y 10: "))
intentos = 3
num = 0
while num != sorpresa and intentos > 0:
    num = int(input("Introduce un número: "))
    intentos -= 1
    if num > sorpresa:
        print("El número es mayor")
    elif num < sorpresa:
        print("El número es menor")
    else:
        print("¡Has acertado!")

if intentos == 0 and num != sorpresa:
    print(f"Lo siento, no te quedan más intentos. El número era {sorpresa}") 