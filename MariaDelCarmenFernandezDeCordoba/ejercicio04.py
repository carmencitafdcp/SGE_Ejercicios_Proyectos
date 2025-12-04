def dibujarCuadrados(n):
    if n <= 0:
        print("No se puede pintar el cuadrado.")
        return 
    for i in range(n):
        estrellitasIzq = '*' * n
        estrellitasderecha = '*' * n
        espacios = ' ' * i
        print(estrellitasIzq + espacios + estrellitasderecha)

num = int(input("¿De cuántas estrellitas quieres que sean tus cuadrados?"))
dibujarCuadrados(num)