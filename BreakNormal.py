#break
n=int(input('Ingrese un numero: '))
for i in range (1,n+1):
    if i %2==0:
        break #termina la funcion a  la que esta inscrita
        #ya sea dentro de un for o while o cualquier otra funcion
        print(i)