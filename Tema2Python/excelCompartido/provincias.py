# Crea un programa que trabaje con ficheros y cumpla los siguientes pasos:
# 1. Crea un fichero llamado provincias.txt desde el propio programa (no vale crearlo previamente en el workspace de VS Code).
# 2. Escribe en él las ocho provincias de Andalucía, cada una en una línea (separadas por retorno de carro).
# 3. Pide al usuario que introduzca su provincia favorita.
# 4. Busca esa provincia dentro del fichero y comprueba si existe. Si existe, muéstrala por pantalla.
# 5. Si no existe, añádela al final del fichero, resaltada con asteriscos (por ejemplo: *Pontevedra*).
# 6. Lee el fichero completo y muestra todas sus líneas una a una por pantalla.
# 7. Por último, vuelve a leer el fichero y muestra únicamente aquellas líneas que contengan la provincia favorita introducida por el usuario.

provincias = ('Sevilla', 'Cadiz', 'Granada', 'Cordoba' , 'Malaga', 'Huelva', 'Almeria', 'Jaen')
provinciaFAV = ''
existe = False
lineas = ''
repetir = "s"

while repetir.lower() == "s":
    f = open('Tema2Python/excelCompartido/provincias.txt', 'w')
    for prvn in provincias:
        f.write(f"{prvn}\n")
    f.close()

    provinciaFAV = input("¿Qué provincia andaluza te gusta más? ")
    f = open('Tema2Python/excelCompartido/provincias.txt')
    lineas = f.readlines()
    f.close()

    for l in lineas:
        if l.strip().lower() == provinciaFAV.lower():
            existe = True

    if existe:
        print(f"\n¡Se ha encontrado tu provincia, es: {provinciaFAV}!")
    else:
        print("\nNo se ha podido encontrar tu provincia, así que la añadiremos resaltada.")
        f = open('Tema2Python/excelCompartido/provincias.txt', 'a')
        f.write(f"*{provinciaFAV}*\n")
        f.close()

    print("\nCONTENIDO DEL FICHERO: ")
    f = open('Tema2Python/excelCompartido/provincias.txt')
    for l in f:
        print(l.strip())
    f.close()

    print("\nSOLO LÍNEAS CON TU PROVINCIA: ")
    f = open('Tema2Python/excelCompartido/provincias.txt')
    for l in f:
        if provinciaFAV.lower() in l.lower():
            print(l.strip())
    f.close()

    repetir = input("¿Deseas continuar añadiendo o buscando provincias? (s/n) ")