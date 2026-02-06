class ContadorCalorias:
    def __init__(self):
        self.yogures = []
    
    def anadir_yogur(self, yogur):
        self.yogures.append(yogur)
    
    def calorias_conjunto(self):
        return sum(y.calorias() for y in self.yogures)
    
    def calorias_tipo(self, tipo):
        return sum(y.calorias() for y in self.yogures if y.tipo == tipo.lower())