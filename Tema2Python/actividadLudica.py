provincias = ['Huelva', 'Sevilla', 'Cadiz', 'Córdoba', 'Málaga', 'Granada', 'Jaén', 'Almería']

# 1. Eliminar una que no tenga costa

provincia = provincias.pop(3)
print("Se ha eliminado " + provincia)

# 2. Ordenar las que quedan alfabéticamente

provincias.sort()
print(provincias)

# 3. Elegir nuestra provincia favorita de las que quedan

fav = 'Cádiz'
provincias.insert(0, fav)
print(provincias)

# 4. Nos cargamos las 2 provincias que estén en medio

provincias[3:5] = []
print(provincias)

# 5. Multiplicar el numero de ocurrencias de la provincia favorita

for i in range(0,2):
    provincias.insert(i, fav)
print(provincias)

# 6. Contar el numero de veces que se repite la más repetida

max = 0

for i in provincias:
    num = provincias.count(i)
    if max < num:
        max = num

provinciaMax = ''
for i in provincias:
    if max == provincias.count(i):
        provinciaMax = i

print(provinciaMax)

# 7. Eliminar el elemento que tenga como indice la provincia máxima
eliminada = provincias.pop(provincias.count(provinciaMax))
print("La provincia eliminada es: " + eliminada)
print(provincias)

# 8. Dar la vuelta a la lista

provincias.reverse()
print(provincias)

#9. Quitar las dos últimas

provincias[5:7] = []
print(provincias)