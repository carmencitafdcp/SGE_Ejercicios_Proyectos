def triangulo(filas):
    cols = 1
    while cols <= filas:
        print("*" * cols)
        cols += 1
    cols = filas - 1
    while cols >= 1:
        print("*" * cols)
        cols -= 1
print("¡Hola! Vamos a hacer la mitad de un rombo de estrellitas.")
print(triangulo(5))

