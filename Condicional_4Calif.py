#Calificacion de notas
#Datos:
# n -> notas
# r -> respuesta

n = float(input('Ingrese su nota: '))
if n <=50:
    r='Reprobado'
elif n<=80:
    r='Aprobado'
elif n<=90:
    r='Sobresaliente'
else:
    r='Excelente'
print('Su nota: ',n, r)