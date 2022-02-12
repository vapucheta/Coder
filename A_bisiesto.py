import sys

if len(sys.argv) != 2:
    print("Fv ingresar un año")
    exit()

while True:
    try:
        vari1 = int(sys.argv[1])
        def anio_bisiesto(vari1):
            if vari1 % 100 == 0 and vari1 % 400 != 0:
                print("El año", vari1,"no es bisiesto")
            elif vari1 % 4 == 0:
                print ("El año",vari1,"es bisiesto")
            else:
                print ("El año",vari1,"no es bisiesto")
            return vari1
        
        anio_bisiesto(int(vari1))
        break
    except:
        print("No ingresó un número")
        exit()
