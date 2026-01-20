import math

class Figura:
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    def calcularArea(self):
        pass
    
    def calcularPerimetro(self):
        pass
    
    def calcularFactorEscala(self, num:float):
        pass

class Rectangulo(Figura):
    def __init__(self, nombre:str, base:float, altura:float):
        super().__init__(nombre)
        self.base = base
        self.altura = altura
        
    def calcularArea(self) -> float:
        area = self.base * self.altura
        return area
    
    def calcularPerimetro(self) -> float:
        perimetro = 2 * self.base + 2 * self.altura
        return perimetro
    
    def calcularFactorEscala(self, num:float):
        self.base = self.base * num
        self.altura = self.altura * num

class Circulo(Figura):
    def __init__(self, nombre:str, radio:float):
        super().__init__(nombre)
        self.radio = radio
        
    def calcularArea(self) -> float:
        area = math.pi * self.radio ** 2
        return area
    
    def calcularPerimetro(self) -> float:
        perimetro = 2 * math.pi * self.radio
        return perimetro
    
    def calcularFactorEscala(self, num:float):
        self.radio = self.radio * num

class Triangulo(Figura):
    def __init__(self, nombre:str, base:float, altura:float):
        super().__init__(nombre)
        self.base = base
        self.altura = altura
    
    def calcularArea(self) -> float:
        area = (self.base * self.altura) / 2
        return area
    
    def calcularPerimetro(self) -> float:
        perimetro = self.base * 3
        return perimetro
    
    def calcularFactorEscala(self, num:float):
        self.base = self.base * num
        self.altura = self.altura * num
        
figuras = [
    Rectangulo('Rectangulo', 2, 4),
    #...
]

area_total = sum(f.calcularArea() for f in figuras)
print()
perimetro = sum(f.calcularPerimetro() for f in figuras)
print()




        
        

    
