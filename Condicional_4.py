#Opcion A (if - else)
#Verificar si un numero es positivo, negativo o nuetro
'''
a= int(input('Ingrese un numero: '))
if a < 0:
    r='Negativo'
else:
    if a==0:
        r='Neutro'
    else:
        r='Positivo'
print('El numero es: ', r)
'''
#Opcion B (elif)
#Verificar si un numero es positivo, negativo o nuetro
b=int(input('2 Ingrese un numero: '))
if b<0:
    r='Negativo'
elif b==0:
    r='Neutro'
else:
    r='Positivo'
print('El numero es: ', r)