#Codigo que te pregunte el nombre y lo repita las veces que quieras

name = input('Introduce tu nombre: ')
rep = int(input('Veces que quieres que se repita: '))

def repeticion():
    i = rep
    while i>0:
        print(name)
        i=i-1

repeticion()