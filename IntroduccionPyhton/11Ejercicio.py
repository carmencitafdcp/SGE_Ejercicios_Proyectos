objetivo = int(input("Hola! Por favor, introduce un número entero: "))
num = 0
listaNums = []

while (objetivo != num):
    aux = int(input("Introduce un número: "))
    num += aux
    print(f'el objetivo total es {objetivo} y aún vas por {num} te queda {objetivo-num}')
    if(num > objetivo):
        print(f'Te has pasado del objetivo, la meta era {objetivo}')
        num-=aux
        print(f'Se ha quitado el aporte más reciente añadido, vuelves a estar en {num}.')
    else:
        listaNums.append(aux)
print("¡Enhorabuena! Has alcanzado el objetivo!")
print(listaNums)