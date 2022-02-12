#2) Realiza una función llamada area_circulo() que devuelva el área de un círculo
# a partir de un radio. Calcula el área de un círculo de 5 de radio

import math

def area_circulo(radio, pi):
    resultado = (radio**2)*math.pi
    return resultado

resultado_area_circulo = area_circulo(5, math.pi)
print(resultado_area_circulo)