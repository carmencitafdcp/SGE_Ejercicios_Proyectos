def ordenada (primero, segundo, tercero, cuarto, quinto, sexto):
    lista = [primero, segundo, tercero, cuarto, quinto, sexto]
    lista_dos = []
    maximo = max(lista)
    minimo = min(lista)
    mayor = []
    menor = []
    for n in lista:
        if n == maximo:
            mayor.append(n)
        elif n == minimo:
            menor.append(n)
    lista_dos = menor
    for n in lista:
        if n != minimo and n != maximo:
            lista_dos.append(n)
    lista_dos = lista_dos + mayor
    return lista_dos

primero = int(input("Escribe el primer número: "))
segundo = int(input("Ahora el segundo: "))
tercero = int(input("Ahora el tercero: "))
cuarto = int(input("Ahora el cuarto: "))
quinto = int(input("Ahora el quinto: "))
sexto = int(input("Ahora el sexto: "))
lista_ordenada = []

lista_ordenada = ordenada(primero, segundo, tercero, cuarto, quinto, sexto)
print(lista_ordenada)