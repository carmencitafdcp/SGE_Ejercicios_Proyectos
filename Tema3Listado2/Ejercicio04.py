import random

def tirarDado():
    return random.randint(1, 6)

def Ciradas(numTiradas):
    return [tirarDado() for _ in range(numTiradas)]

def vecesNumSalido(tiradas, numero):
    cont = 0
    for tirada in tiradas:
        if tirada == numero:
            cont += 1
    return cont 

def porcentajesSegunTiradas(tiradas, numero):
    total = len(tiradas)
    veces = vecesNumSalido(tiradas, numero)
    if total > 0:    
        return (veces / total) * 100 
    else:
        return 0   
