def calcularNota (notas):
    total = 0
    for clave, valor in notas.items():
        if len(valor) > 1:
            suma = sum(valor)
            total += suma/len(valor)
        else:
            total += valor[0]
    media = total/len(notas)
    return media

notas = {6.1 : [9.6, 3], 6.2 : [7.25], 6.3 : [8.7]}
print(f"Tu nota es: {calcularNota(notas)}")