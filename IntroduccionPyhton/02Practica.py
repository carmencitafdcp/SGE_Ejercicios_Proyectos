aleatorio = random.randint(1, 50)
intentos = 5
intento = 0
print("¡Hola! Vamos a jugar a adivinar un número entre 1 y 50.")

while intento <= intentos:
    num = int(input("Adivina el número: "))
    if num < aleatorio:
        print("Ups! tu número es más pequeño.")
    elif num > aleatorio: 
        print("Ups! Te has pasado un poquito.")
    else: 
        print("Enhorabuena has adivinado el número!!")
        break
    intento += 1
    print(f"Te quedan {intentos - intento} intentos.")
