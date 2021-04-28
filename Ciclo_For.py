#El primer ejemplo hace que el ciclo for muestra uno
# por uno los elementos de la cadena dada
for i in ' numero':
    print(i)

#Calcula el numero de vocales de una frase
frase= str(input('Ingrese una frase: '))
vocales='aeiouAEIOU'
contador=0
for i in frase:
    if i in vocales:
        contador=contador+1
print('El numero de vocales es: ',contador)