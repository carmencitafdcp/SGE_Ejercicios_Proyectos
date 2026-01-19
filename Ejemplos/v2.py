from __future__ import annotations

class Pastel():
    #Esto es una función decoradora que sirve para decorar el resultado de ciertos métodos que se declaran en la propia función.
    @staticmethod
    def audit(method):
        #patrón decorador con método wrapper que actúa como envoltorio del método original, envuelve la funcionalidad del método.
        #El método original (aumentar_precio, resetear_precio) se reemplaza por la función wrapper
        #La función wrapper rodea la ejecución del método original con comportamiento adicional
        #Primero ejecuta el print() y luego llama al método original con esto:
        def wrapper(self, *args, **kwargs):
            print(f'Pastel {self.nombre} haciendo {method.__name__}') 
            return method(self, *args, **kwargs) # ESTO
        return wrapper
    
    def __init__(self, nombre: str, precio: int):
        self.nombre = nombre
        self.precio = precio

    def __eq__(self, pastel: Pastel) -> bool:
        return self.precio == pastel.precio

    @audit
    def aumentar_precio(self, precio: int) -> int:
        self.precio = precio + 1

    @audit
    def resetear_precio(self):
        self.precio = 0.0

    
pastel_1 = Pastel('Tarta', 20)
pastel_2 = Pastel('Flan', 20)

print(f'{pastel_1 == pastel_2}')

print(f'{pastel_1.aumentar_precio(20)}')
print(f'{pastel_1.resetear_precio()}')




    