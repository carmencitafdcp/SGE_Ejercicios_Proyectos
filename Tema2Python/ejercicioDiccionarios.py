# Estoy dando clases de inglés para el B2 y me gustaría que me ayudarais a crear un diccionario para ver cómo
# se dicen palabras con significado “raro” españolas en inglés. Se hará todo en el mismo archivo, no se crean
# clases. Por ejemplo, “Cabeza: (en el sur de España) amigo/colega”, aro: sí, de acuerdo. Consideraremos que
# no se repiten palabras con el mismo nombre, es decir, que la palabra “take” no aparece dos veces en el
# diccionario y que, si tiene varios significados, estos pueden ir en el mismo String “significado”, por ejemplo,
# for---->por, para, durante.
# Se debe utilizar un diccionario que se puede instanciar con algunos elementos de inicio y un menú para cada
# uno de las siguientes funcionalidades:
# • Agregar una nueva palabra por teclado.
# • Imprimir el diccionario completo “en bonito”.
# • Buscar una palabra por nombre y mostrar su significado evitando que salta un error si la palabra no se
# encuentra.
# • Modificar una palabra, modificando únicamente el significado de esta por otro nuevo, leído por
# teclado.
# • Pedir al usuario sus dos palabras favoritas con los significados y combinar este con el ya creado
# modificando el original.
# • Borrar una palabra (ustedes decidís la mejor forma).
# • Ordenar el diccionario por orden alfabético.

# Estoy dando clases de inglés para el B2 y me gustaría que me ayudarais a crear un diccionario para ver cómo
# se dicen palabras con significado "raro" españolas en inglés. Se hará todo en el mismo archivo, no se crean
# clases. Por ejemplo, "Cabeza: (en el sur de España) amigo/colega", aro: sí, de acuerdo. Consideraremos que
# no se repiten palabras con el mismo nombre, es decir, que la palabra "take" no aparece dos veces en el
# diccionario y que, si tiene varios significados, estos pueden ir en el mismo String "significado", por ejemplo,
# for---->por, para, durante.
# Se debe utilizar un diccionario que se puede instanciar con algunos elementos de inicio y un menú para cada
# uno de las siguientes funcionalidades:
# • Agregar una nueva palabra por teclado.
# • Imprimir el diccionario completo "en bonito".
# • Buscar una palabra por nombre y mostrar su significado evitando que salta un error si la palabra no se
# encuentra.
# • Modificar una palabra, modificando únicamente el significado de esta por otro nuevo, leído por
# teclado.
# • Pedir al usuario sus dos palabras favoritas con los significados y combinar este con el ya creado
# modificando el original.
# • Borrar una palabra (ustedes decidís la mejor forma).
# • Ordenar el diccionario por orden alfabético.

Esp_Ing = {
    'Cabeza' : 'Amigo, parte superior del cuerpo humano, parte principal o inicial de algo ,líder' , 
    'aro' : 'Circunferencia, sí, claro, de acuerdo', 
    'piquislabis' : 'tentempié'
}

repetir = True
opcion = 0
palabraNueva = ''
significadoNuevo = ''
clave = ''
significado = ''
palabra = ''
pab1 = ''
sig1 = ''
pab2 = ''
sig2 = ''
pabsFavs = ''
dicOrdenado = ''

while  repetir:
    print("Bienvenido a tu diccionario.")
    print("1. Agregar una nueva palabra por teclado.")
    print("2. Imprimir el diccionario completo /'en bonito/'.")
    print("3. Buscar una palabra por nombre y mostrar su significado evitando que salta un error si la palabra no se encuentra.")
    print("4. Modificar una palabra, modificando únicamente el significado de esta por otro nuevo, leído por teclado.")
    print("5. Pedir al usuario sus dos palabras favoritas con los significados y combinar este con el ya creado modificando el original..")
    print("6. Borrar una palabra (ustedes decidís la mejor forma).")
    print("7. Ordenar el diccionario por orden alfabético.")
    print("8. Salir.")
    opcion = int(input("Escoge tu opción: "))
    match opcion:
        case 1:
            print('Vamos a añadir una palabra nueva al diccionario.')
            palabraNueva = input("¿Qué palabra quieres añadir? ")
            significado = input("¿Cuál es su significado? ")
            Esp_Ing[palabraNueva] = significado
            print(Esp_Ing)
        case 2:
            for clave, significado in Esp_Ing.items():
                print(f'{clave}: {significado}')
        case 3:
            palabra = input("¿Qué palabra deseas buscar? ")
            if palabra in Esp_Ing.items():
                print(f"Signidicado: {Esp_Ing[palabra]}")
        case 4:
            palabra = input("¿Qué palabra deseas modificar? ")
            if palabra in Esp_Ing.items():
                significado = input("¿Qué significado nuevo le quieres poner? ")
                Esp_Ing[palabra] = significado
                print(f"Palabra modificada: {Esp_Ing[palabra]}")
        case 5:
            pab1 = input("Dime tu palabra favorita del diccionario: ")
            sig1 = input("Y su significado: ")
            pab2 = input("Ahora otra palabra: ")
            sig2 = input("Su significado: ")
            pabsFavs = {pab1:sig1, pab2:sig2}
            print(Esp_Ing)
        case 6:
            palabra = input("Dime una palabra para eliminar: ")
            if palabra in Esp_Ing:
                Esp_Ing.pop(palabra)
            print(Esp_Ing)
        case 7:
            print('Diccionario ordenado alfabéticamente.')
            dicOrdenado = dict(sorted(Esp_Ing.items()))
            print(dicOrdenado)
        case 8:
            print('Hasta pronto.')
        case _:
            print('Unknown option.')
