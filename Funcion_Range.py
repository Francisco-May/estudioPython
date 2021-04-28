#hacer una tabla de multiplicar del 1 al 10 con for
n=int(input('Ingrese un numero: '))
for i in range(1,11):
    print(n,'x',i,'=',n*i)
    print('{}x{}='.format(n,i),n*i)
''' Tener en cuenta que cuando se usa la funcion range hay tres variaciones
la primera variacion es 
RANGE(a): la cual indica el numero de elementos ingresados, ejemplo
range(4) => {1,2,3,4} (el total de elementos es 4 correctamente)
la segunda variacion es:
RANGE(a,b): la cual indica desde que numero empieza y hasta cual termina, sin
embargo hay qe tener en cuenta que termina un numero antes del puesto, ejemplo
range(2,6)=> {2,3,4,5} (teniendo en cuenta empieza en 2 pero termina en 5 debido
a que como bien se explico, el 6 esta siendo ignorado por aparecer como limite)
la tercera variacion es:
RANGE(a,b,c): la cual nos indica con que numero empieza (a), hasta que numero
llegara siempre sin contarlo (b) y cuanto es el incremento que tendra (c), ejemplo
range(3,9,2)=> {3,5,7} (de manera que empieza en 3, le sigue 5 por que a+c que 
es 3+(1*2)=5, y luego 7 porque a+c es 3+(2*2)=7, por ultimo 9 pero este esta
puesto como limitante por tanto no se muestra)'''