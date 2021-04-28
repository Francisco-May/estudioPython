#Serien fibonacci
'''Ejemplo:
w1+w2=suma
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
3 + 5 = 8
5 + 8 = 13
8 + 13 = 21
'''
# w = interruptor (w1,w2)
# c = contador
n=int(input('Ingrese un numero: \n'))
w1= 0
w2=1
suma=0
c=0
if n<=0:
    print('Error')
elif n==1:
    print(w1)
else:
    #print(w1,'+',w2,'=',suma)
    suma = w1 + w2
    while c < n:
        #print(w1) #este lo saque pero al hacer la lista empieza en cero asi qe no
        #print(w2) #este lo puse pa que saqe correcta la lista
        #print(w1,'+ "',w2,'"=',suma) #este es la escalera de suma fibonacci
        print(f'{w1}+ "{w2}" ={suma}') #este es la escalera de suma fibonacci
        suma = w1 + w2
        #actualizar los datos
        w1=w2
        w2=suma
        suma=w1+w2
        c += 1  # c=c+1 (esto es lo mismo)