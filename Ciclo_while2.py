#tabla de multiplicar
n=int(input('Ingrese la tabla que desea ver: '))
i=1
while i<=10:
    print('{} x {}='.format(n,i),n*i)
    #igual esta puede ser: print(n,'x',i,'=',n*i)
    i=i+1
print('Tabla de multiplicar del: ',n)