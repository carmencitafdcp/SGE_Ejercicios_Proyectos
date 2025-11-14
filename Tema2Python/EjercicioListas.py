recaudaciones = [0.0, 123.0, 180.5, 95.8, 100.1, 0.0, 0.0, 200.8, 143.0]
option = 0
repetir = True
recaudacion = 0.0 
index = 0
max_val = 0.0
dias = []
dia = 0
cantidad = 0.0
suma = 0.0
ordenada = []
media = 0.0
porcentaje = 0
contador = 0
total = 0

while repetir:
    print("**Bienvenido a este menú para recuadaciones**")
    print("1. Agregar nueva recaudación.")
    print("2. Poner a cero una recaudación (el cliente no pagó)")
    print("3. Imprimir todas las recaudaciones.")
    print("4. Buscar el día con mayor recaudación y cuántos días se ha ganado dicha recaudación.")
    print("5. Sumar una cantidad a un día como gasto extra.")
    print("6. Calcular el total de la recaudaciones.")
    print("7. Ordenar la lista de menor a mayor.")
    print("8. Calcular la media diaria.")
    print("9. Calcular el porcentaje de días al mes con la habitación alquilada.")
    print("10. Dividir la lista en dos, una con las 5 recaudaciones más bajas y otra con las restantes.")
    print("11. Salir.")
    option = int(input("Escoge una opción: "))
    match option:
        case 1:
            recaudacion = float(input("¿Cuánto has ganado hoy? "))
            recaudaciones.append(recaudacion)
            print(recaudaciones)
        case 2:
            index = int(input("¿Qué recaudación no ha sido cobrada? (Pon el índice)"))
            if index >= 0 and index < len(recaudaciones):
                del recaudaciones[index]
            print(recaudaciones)
        case 3:
            for recaudacion in recaudaciones:
                print(f"{recaudacion}")
        case 4:
            max_val = max(recaudaciones)
            for i, v in enumerate(recaudaciones):
                if v == max_val:
                    dias.append(i + 1)  
            print(f"La mayor recaudación es {max_val} y se alcanzó {len(dias)} vez/veces.")
        case 5:
            cantidad = float(input("¿Qué cantidad deseas sumar?"))
            dia = int(input("¿Y a qué día en concreto? (índice)"))
            suma = recaudaciones[dia] + cantidad
            print(f"Ahora recaudaste {suma} en el día {dia}.")
        case 6:
            for recaudacion in recaudaciones:
                suma = suma + recaudacion
            print(f"La suma total es: {suma}")
        case 7:
            ordenada = sorted(recaudaciones)
            print(f"Lista ordenada de menor a mayor: {ordenada}")
        case 8:
            for recaudacion in recaudaciones:
                suma = suma + recaudacion
            media = suma / len(recaudaciones) 
            print(f"La media es {media}")
        case 9:
            total = len(recaudaciones)
            for recaudacion in recaudaciones:
                if recaudacion != 0.0:
                    contador +=1 
                
            if total > 0:
                porcentaje = (contador/total)*100
                print(f"El porcentaje de días con recaudación es {porcentaje}")
        case 10:
            print()
        case 11:
            print()
        case _:
            print("Unknown choice.")
        