#Mayor que el anterior (\ se saca con alt + 92)
valor=int(input('¿Cuantos valores va a introducir?\n '))
if valor<1:
    print('Error')
else:
    primero = int(input('Escriba un numero: '))
    for i in range(valor-1):
        num=int(input(f'Escribe un numero mas grande que {primero}: \n'))
        print(i)
        if num <=primero:
            print(f'El {num} no es mayor que el {primero}')
        else:
            primero = num
    print('Gracias por su colaboracion')