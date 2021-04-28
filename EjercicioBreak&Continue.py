#Seleccionar impares y terminar al encontrar el primero num divisible entre 6
n=int(input('Ingrese un numero: \n'))
for i in range(1,n+1):
    if  not (i %2) & (i%6):
        continue #su funcion correcta es saltarse todo el resto de instrucciones hasta la siguiente funcion
    elif i%7==0:
        break
    print(i)