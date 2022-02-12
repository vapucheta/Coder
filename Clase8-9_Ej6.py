#6) Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas.
#La primera con los números pares, y la segunda con los números impares:
#🖐 Ayuda: Para ordenar una lista automáticamente puedes usar el método .sort()

lista=[6,5,2,1,7] 
par=[] 
impar=[] 

def separar(lista): 
    for n in lista: 
        if n % 2 == 0: 
            par.append(n) 
        else:
            impar.append(n) 
    return par, impar

print(separar(lista)) 

