#A=[1,2,3,4]
a=[1,2,3,4]
print(a)
a=[1,2,3,4,'python',2.6]
print(a[2]) # indica el elemento a buscar en dicha posicion
b=[6,9,7,10]
print(a+b)
c=[25,35,40,85]
print(a+b+c)
#suma todos lo elementos de lista en una sola
#ahora para el sig ejemplo vamos a combinar listas sobre listas
#1ro combinar todas las lista en una sola identificando en una sola
L=[a,b,c]
print(L,'\n')
#ahora bien una vez teniendo esto, podemos buscar mediante filas y columnas
a=[1,2,3,4]
b=[6,9,7,10]
c=[25,35,40,85]
l=[a,b,c]
print('lista L \n',l)
print(l[0][0])
#el primer elemento es fila y el segundo es columnas
print(l[2][3])
print(l[2][2])

