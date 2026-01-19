from __future__ import annotations

class Pastel():
    @staticmethod
    def audit(method):
        def wrapper(self, *args, **kwargs):
            print(f'Pastel {self.nombre} haciendo {method.__name__}')
            return method(self, *args, **kwargs)
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




    