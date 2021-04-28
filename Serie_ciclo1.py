#Serie 4 , 3 , 2 , 1 , 4 , 3 , 2....
#c = controlador (controla elementos)
#w = interruptor en este caso de 4 por ser los elementos de la serie
n= int(input('Ingrese un numero: \n'))
c=0
w= 4
while c < n:
    print(w, end=', ')
    if w > 1:
        w=w-1
    else:
        w=4
    c=c+1