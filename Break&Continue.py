print('identificar pares e impares')
n1= int(input('Escriba un numero: \n'))
n2= int(input(f'Escriba un numero mayor o igual a {n1}: \n'))
if n2<n1:
    print(f'Ingrese un numero mayor o igual que {n1}: \n')
else:
    for i in range(n1,n2+1):
        if i %2==0:
            print(f'El numero {i} es par')
        else:
            print(f'El numero {i} es impar')