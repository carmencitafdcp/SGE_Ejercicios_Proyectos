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



