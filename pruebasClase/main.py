from modelo import Profesor
from modelo import Alumno 
from gestion import Aula

def main():
    profesor = Profesor("Ana García", "Matemáticas")
    
    aula = Aula("1º Bachillerato A", profesor)
    
    alumno1 = Alumno("Carmen", 4.5)
    alumno2 = Alumno("Luis", 3.8)
    alumno3 = Alumno("Sofía", 6.0)
    
    aula.agregar_alumno(alumno1)
    aula.agregar_alumno(alumno2)
    aula.agregar_alumno(alumno3)
    
    print(aula)
    print(f"Nota media del aula: {aula.calcular_nota_media():.2f}")
    
if __name__ == "__main__":
    main()