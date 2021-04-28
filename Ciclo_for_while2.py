#La suma de los primeros n numeros
n=int(input('Ingrese un numero: \n'))
suma=0
for i in range(1,n+1):
    suma=suma+i
print('La suma de los primeros ',n, ' es: ',suma)