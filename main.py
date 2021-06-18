import numpy as np
print('Solucion primer paso del reto numero 6')
print('Paso cambio de columnas en una matriz')
print('')
#creacion de matriz
m = np.arange(20).reshape(4, 5)

print(m)
print('--------------------------------------')
#cambio de columnas
x=m[:,[3,1,2,0,4]]

print(x)

print('')
print('')

print('Solucion segundo paso del reto numero 6')
print("Paso cambio de filas en una matriz")
print('')
#copia de matriz (m)
print(m)

y=m[[3,2,1,0],:]
print('--------------------------------------')
print(y)