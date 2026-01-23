class Yogur:
    CAL_100ML = 120.5
    
    def __init__(self, tipo: str, tamano_ml: float):
        self.tipo = tipo.lower()
        self.tamano_ml = tamano_ml
    
    def calorias(self) -> float:
        base = (Yogur.CAL_100ML * self.tamano_ml) / 100
        if self.tipo == "desnatado":
            return base * 0.7
        elif self.tipo == "proteico":
            return base + 50
        return base

class ContadorCalorias:
    def __init__(self):
        self.yogures = []
    
    def anadir_yogur(self, yogur):
        self.yogures.append(yogur)
    
    def calorias_conjunto(self):
        return sum(y.calorias() for y in self.yogures)
    
    def calorias_tipo(self, tipo):
        return sum(y.calorias() for y in self.yogures if y.tipo == tipo.lower())

class Main:
    def __init__(self):
        self.contador = ContadorCalorias()
    
    def ejecutar(self):
        n = int(input("Número yogures: "))
        for _ in range(n):
            tipo = input("Tipo: ").lower()
            ml = float(input("ml: "))
            yogur = Yogur(tipo, ml)
            self.contador.anadir_yogur(yogur)
        
        print(f"TOTAL: {self.contador.calorias_conjunto():.1f}")
        print(f"Normal: {self.contador.calorias_tipo('normal'):.1f}")
        print(f"Desnatado: {self.contador.calorias_tipo('desnatado'):.1f}")
        print(f"Proteico: {self.contador.calorias_tipo('proteico'):.1f}")

Main().ejecutar()
