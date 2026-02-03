def getint() -> int:
    try:
        num = input(int("Dame un número entero: "))
        return num
    except ValueError:
        print(f"Error: ese no es un número entero!")
    

getint()