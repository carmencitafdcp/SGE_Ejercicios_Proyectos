# def intdiv(a: int, b: int) -> int:
#     try:
#         return a // b
#     except:
#         print("Please do not divide by zero... ")

# intdiv(5,0)

def division(a, b):
    try:
        return a // b
    except (TypeError, ZeroDivisionError):
        print("Check operands. Some of them seem wrong...")
    except Exception:
        print("Ups! Something went wrong")
        
division(0,0)

values = [4, 2, 7]

try:
    r = values[2]
except IndexError:
    print("Error: El índice no existe.")
else: 
    print(f"Perfecto! Aquí está el número {r}")
finally:
    print("Hola buenas, just cheking...")

def _sum(a: int, b: int) -> int:
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    raise TypeError('Operands must be integers')

_sum(0,'h')