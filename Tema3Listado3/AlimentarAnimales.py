class Animal:
    anio = 365
    
    def __init__(self, coste: float):
        self.coste = coste
        
    def coste_anual(self) -> float:
        return self.coste * Animal.anio
    
class Oso(Animal):
    def __init__(self, coste: float, coste_carne_semanal: float):
        
    





















# class Animal:
#     DIAS_ANIO = 365
    
#     def __init__(self, coste_diario: float):
#         self.coste_diario = coste_diario
    
#     def coste_anual(self) -> float:
#         return self.coste_diario * Animal.DIAS_ANIO

# class Oso(Animal):
#     def __init__(self, coste_diario: float, coste_carne_semanal: float):
#         super().__init__(coste_diario)
#         self.coste_carne_semanal = coste_carne_semanal
    
#     def coste_anual(self) -> float:
#         normal = super().coste_anual()
#         carne = self.coste_carne_semanal * 52 * 2
#         return normal + carne

# class Serpiente(Animal):
#     def __init__(self, coste_diario: float, coste_insecto: float, insectos_semana: int):
#         super().__init__(coste_diario)
#         self.coste_insecto = coste_insecto
#         self.insectos_semana = insectos_semana
    
#     def coste_anual(self) -> float:
#         normal = super().coste_anual()
#         insectos_anuales = self.insectos_semana * 52 * 2
#         return normal + (insectos_anuales * self.coste_insecto)

# class Zoo:
#     def __init__(self):
#         self.animales = []
    
#     def anadir_animal(self, animal):
#         self.animales.append(animal)
    
#     def coste_serie(self, num_normales: int, num_osos: int, num_serpientes: int) -> float:
#         total = 0
        
#         for _ in range(num_normales):
#             total += Animal(5.0).coste_anual()
            
#         for _ in range(num_osos):
#             total += Oso(8.0, 20.0).coste_anual()
            
#         for _ in range(num_serpientes):
#             total += Serpiente(2.0, 0.5, 10).coste_anual()
            
#         return total
    
#     def descuento_proveedor(self, lista_animales: list, umbral: float) -> float:
#         total = sum(a.coste_anual() for a in lista_animales)
#         return total * 0.1 if total > umbral else 0.0
    
#     def gasto_solo_osos(self) -> float:
#         return sum(a.coste_anual() for a in self.animales if isinstance(a, Oso))

# def main():
#     zoo = Zoo()
    
#     print("🦒 ZOOLÓGICO - Costes anuales 🐘")
#     print()
    
#     coste = zoo.coste_serie(5, 3, 2)
#     print(f"1. 5 normales + 3 osos + 2 serpientes = {coste:.2f}€")
    
#     animales = [Animal(5.0) for _ in range(20)]
#     descuento = zoo.descuento_proveedor(animales, 10000)
#     print(f"2. Descuento (>10k€): {descuento:.2f}€")
    
#     zoo.anadir_animal(Oso(8.0, 20.0))
#     zoo.anadir_animal(Oso(10.0, 25.0))
#     print(f"3. Solo osos en zoo: {zoo.gasto_solo_osos():.2f}€")

# main()
