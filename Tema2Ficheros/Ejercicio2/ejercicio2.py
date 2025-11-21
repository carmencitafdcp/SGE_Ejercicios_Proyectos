from datetime import datetime

tiempo = datetime.now()

f = open('Tema2Ficheros/Ejercicio2/horaFecha.txt', 'w')
f.write(f"Fecha: {tiempo.date()}, Hora: {tiempo.time()}")
f.close()