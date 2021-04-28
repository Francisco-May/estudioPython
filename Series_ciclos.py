#Generar los multiplos de 3
#m = interruptor por ser en esta caso el 3
n=int(input('Ingrese un numero: \n'))
m = 3
for i in range(1,n+1):
    print(m , end=', ')#esto sirve para que el resultado salga en horizontal
    m=m+3