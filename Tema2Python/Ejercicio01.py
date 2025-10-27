nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
listaVacia = []
frutas = ["Naranjas", "Peras", "Fresas", "Arándanos"]
hortalizas = ["Lechuga", "Espinacas", "Cebollín", "Calabacín"]

print("------------------------------------")
print("¡Bienvenido al programa!")
print("En este programa voy a explicar algunas funcionalidades con listas en Python.")
print("1. Buscar elementos en la lista.\nPara buscar elementos en la lista se puede usar el índice o bien recorrer la lista y comprobar si el elemento introducido existe.")
print(f"Esta es la lista que tenemos: {nums}")
print("Primero con el índice: ")
indice = int(input("Introduce el índice del elemento que quieres (recuerda que el indexado empieza en 0): "))
print(nums[indice])
print("Ahora a través del elemento exacto que queremos: ")
numBuscar = int(input("Introduce el número que quieras encontrar en la lista nums: "))
if numBuscar in nums:
    print(f"¡Existe! es el: {numBuscar}")
else:
    print("Lo siento ese número no existe en la lista.")
print("------------------------------------")

print("¡Bien! Ahora añadiremos un elemento nuevo a la lista.\nSe puede hacer con .append() al final de la lista o con .insert() en una posición específica.")
print("Primero añadiremos un elemento al final.")
numFinal = int(input("Teclea el número que deseas añadir al final: "))
print(nums.append(numFinal))
print(f"Esta es la lista actualizada: {nums}")
print("Ahora lo añadiremos justo donde queremos, para ello necesitamos escribir el índice seguido de unna coma y el número que deseamos meter.")
num = int(input("¿Qué número nuevo deseas añadir? "))
posicion = int(input("¿En qué posición deseas añadir el nuevo número?"))
print(nums.insert(posicion, num))
print(f"Esta es la lista actualizada: {nums}")
print("------------------------------------")

print("Miramos ahora  cómo partir una lista, esto se suele hacer más para cadenas, pero aquí podemos hacerlo también. ")
print("Para partir una lista debemos usar el índice de inicio, dos puntos y el índice final.\nO también puede ponerse la cantidad de elementos a sacar tras los dos puntos.")
indiceInicio = int(input("Introduce la posición desde donde quieres que comience a trocearse: "))
indiceFinal = int(input("Introduce la posición final: "))
cantidad = int(input("Introduce cuántos elementos quieres sacar en este rango: "))
print("Primero vamos a sacar simplemente el trozo, sin cantidad de elementos.")
print(nums[indiceInicio:indiceFinal])
print("Ahora lo mismo pero especificando una cantidad: ")
print(nums[indiceInicio:cantidad:indiceFinal])
print("------------------------------------")

print("¡¡Estupendo!! Vamos avanzando rápido.")
print("Te preguntarás ahora cómo se puede invertir una lista, ¿no?\nEsto se puede hacer o bien con ::-1 o bien con list(reversed(nums)) o bien .reverse()")
print(f"Vamos a probar la primera que es: nums[::-1] {nums[::-1]}")
print(f"Prosigamos, ahora con reversed, {list(reversed(nums))}")
print(f"Y ahora con la función reverse(): {nums.reverse()}")
print("------------------------------------")

print("Ahora, para crear una lista iniciándola a vacío, necesitamos crear un bucle que le añada los elementos uno a uno.\nSe usa esto:\n" \
"for i in range(20):\n   nums.append(i).")
print("Usemos una lista vacía: ")
for i in range(20):
    listaVacia.append(i)
print(f"Esta es la lista rellenada: {listaVacia}")
print("------------------------------------")

print("¿Cómo se puede repetir los elementos de una lista? Pues con el signo de multiplicación. Así nums * 3.")
print(nums * 3)
print("------------------------------------")

print("Las listas se pueden combinar con otras listas, mediante el operador +, mediante .extend(), o mediante .append()")
print(f"La primera: {frutas+hortalizas}")
print(f"La segunda: {frutas.extend(hortalizas)}")
print(f"La tercera: {frutas.append(hortalizas)}")
print("------------------------------------")

print("Veamos ahora cómo modificar listas.\nSe puede usar el índice para añadir un nuevo elemento, nums[12]=100.\nO se puede modificar con troceado también, nums[3:5]=[8,9]")
print("Comprobemos la primera opción:")
nums[12] = 100
print(nums)
print("Ahora la segunda opción: ")
nums[3:5] = [8,9]
print(nums)
print("------------------------------------")

print("Para convertir una lista a cadena tienes que usar el método str() y después imprimirlo.")
print("Vamos a probarlo con la lista nums: ")
cadena = str(nums)
print(cadena)
print("------------------------------------")
#convertir lista a cadena