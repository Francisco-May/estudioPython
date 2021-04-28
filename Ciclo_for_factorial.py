#hallar el factorial de un numero cualquiera
#ejemplo
#2! = 1*2= 2
#3! = 1*2*3=6
#8!= 1*2*3*4*5*6*7*8= 40320
n=int(input('Ingrese el numero que quiera conocer su factorial: \n'))
if n<=0:
    print('Ingrese un numero positivo')
else:
    facto = 1
    for i in range(1, n + 1):
        facto = facto * i
    print('El factorial del numero ', n, ' es: ', facto)
    print(f'El factorial del numero {n} es: {facto}')