repetir = True
option = 0
lineas = ""
maxLength = 0

f = open("Tema2Ficheros/Ejercicio6/texto.txt")

while repetir:
    print("**Bienvenido a este menú**")
    print("1. Encontrar la palabra más larga.")
    print("2. Contar cuántas veces sale una palabra en específico.")
    print("3. Leer una línea aleatoria del archivo.")
    print("4. Buscar la palabra más corta.")
    print("5. Ordenar las palabras de menos larga a más larga.")
    print("6. Salir.")
    option = input("Selecciona una opción: ")
    match option:
        case 1:
            lineas = f.readlines()
            for linea in lineas:
                maxLength = len(linea)
                if len(linea) > maxLength:
                    print(f"La palabra más larga es {linea}")
            print()
        case 2:
            print()
        case 3:
            print()
        case 4:
            print()
        case 5:
            print()
        case 6:
            print()
        case _:
            print()