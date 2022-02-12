#1) Realiza una función llamada area_rectangulo() que devuelva el área del rectángulo a partir de una base y
#una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura

import sys
argumentos = sys.argv
if len(argumentos) != 3:
    print("Error: numero de argumentos incorrecto")
    sys.exit(1)
def area_rectangulo(numero1, numero2):
    # Acciones a realizar
    if type(numero1) != int or type(numero2) != int:
        resultado = "Error: los argumentos no son numeros"
    else:
        resultado = numero1 * numero2
    return resultado
resultado_suma = area_rectangulo(int(argumentos[1]), int(argumentos[2]))
print(resultado_suma)