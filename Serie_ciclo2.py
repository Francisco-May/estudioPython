#Serie   A B A B A B A B A......
#w = interruptor para indicar qe elemento sigue, modificando este mismo
n= int(input('Ingrese un numero: \n'))
w= 0
for i in range(1,n+1):
    if w==0:
        print('A',end=', ')
        w=1
    else:
        print('B',end=', ')
        w=0