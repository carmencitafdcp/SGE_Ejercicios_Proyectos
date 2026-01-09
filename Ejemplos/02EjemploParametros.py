def mostrarNotas(nombre, edad=22, *notas):
    print(f"Mi nombre es: {nombre}")
    print(f"Tengo: {edad} años")
    
    if notas:
        print(f"Mis notas son: {notas}")
        promedio = sum(notas) / len(notas)
        print(f"Y mi media es: {promedio}")
    else:
        print("No tengo notas.")
    
mostrarNotas("Carmen", 22, 8, 10, 2, 5)