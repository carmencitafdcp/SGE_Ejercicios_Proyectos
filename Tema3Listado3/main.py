from model import Yogur
from service import ContadorCalorias

class NotIntError(Exception):
    def __init__(self, message = '¡Aquí se debe trabajar con enteros!'):
        super().__init__(message)

class Main:
    def __init__(self):
        self.contador = ContadorCalorias()
        self.tipos = ['normal', 'desnatado', 'proteico']
        
    def ejecutar(self):
        n = int(input("¿Cuántos yogures quieres añadir?: "))
        if not isinstance(n, int):
            raise NotIntError()
        for _ in range(n):
            print(f"Introduce un yogurt → ")
            tipo = input("Tipo: ").lower()
            ml = float(input("ml: "))
            yogur = Yogur(tipo, ml)
            self.contador.anadir_yogur(yogur)
        
        print(f"TOTAL: {self.contador.calorias_conjunto():.1f}")
        print(f"Normal: {self.contador.calorias_tipo('normal'):.1f}")
        print(f"Desnatado: {self.contador.calorias_tipo('desnatado'):.1f}")
        print(f"Proteico: {self.contador.calorias_tipo('proteico'):.1f}")

if __name__ == "__main__":
    Main().ejecutar()