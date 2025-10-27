#3. Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre
#0 y 10). A continuación, debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

notas = []

for i in range(5):
    while True:
        try:
            nota = float(input(f"Introduce la nota {i+1} (0 a 10): "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Por favor, introduce un número válido.")

print("\nNotas introducidas:", notas)
print("Nota media:", sum(notas) / len(notas))
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))


