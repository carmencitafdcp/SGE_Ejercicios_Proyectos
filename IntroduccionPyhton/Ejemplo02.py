year = int(input("Introduce un año:"))

while year == 0 or year < 0:
    print("Debes añadir un año")
    year = int(input("Introduce un año:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):    
    print("Es Bisiesto")
else:
    print("No es Bisiesto")