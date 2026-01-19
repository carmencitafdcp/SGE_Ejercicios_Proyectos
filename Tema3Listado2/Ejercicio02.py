import math

def calculadora():
    n = int(input("Introduce un número positivo: "))
    print("Elige la función que desees hacer:")
    print("1 - seno")
    print("2 - coseno")
    print("3 - tangente")
    print("4 - exponencial")
    print("5 - logaritmo neperiano")
    opcion = input("Escoge una opción: ")

    if opcion == "1":
        funcion = math.sin
        nombre = "seno"
    elif opcion == "2":
        funcion = math.cos
        nombre = "coseno"
    elif opcion == "3":
        funcion = math.tan
        nombre = "tangente"
    elif opcion == "4":
        funcion = math.exp
        nombre = "exponente"
    elif opcion == "5":
        funcion = math.log 
        nombre = "logaritmo"
    else:
        print("Usps! Inténtalo de nuevo.")
        return

    print(f"\nTabla de {nombre}(x) de 1 a {n}:")
    print(f"{'x':>5} | {nombre}(x)")
    print("-" * 25)
    for x in range(1, n + 1):
        resultado = funcion(x)
        print(f"{x:5d} | {resultado:.6f}")
