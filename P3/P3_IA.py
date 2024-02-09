import numpy as np
import matplotlib.pyplot as plt
import math

semilla = int(input("Ingresa el valor de la semilla a utilizar: "))
N = 10
np.random.seed(semilla)
clase1 = np.zeros((N,2))
clase2 = np.zeros((N,2))

#Se obtienen los 10  
for i in range(0,10):
  clase1[i,0] = np.random.rand()+np.sin(np.random.rand())
  clase1[i,1] = np.random.rand()+np.cos(np.random.rand())
  clase2[i,0] = np.random.rand()+np.sin(np.random.rand())
  clase2[i,1] = np.random.rand()+np.cos(np.random.rand())

plt.scatter(clase1[:,0],clase1[:,1],marker='*',color = 'red', alpha=0.8, label ='Clase A') #Se colocan los puntos de la clase A en el gráfico
plt.scatter(clase2[:,0],clase2[:,1],marker='s',color = 'blue', alpha=0.8, label ='Clase B') #Se colocan los puntos de la clase B en el gráfico

x = float(input("Ingresa la coordenada en x: ")) 
y = float(input("Ingresa la coordenada en y: "))


nuevo_punto = [x, y] #Se crea el nuevo punto con las coordenadas ingresadas
plt.scatter(x, y, color = 'green') #Se agrega el punto al gráfico con los otros puntos
plt.legend(loc="best") #Se colocan las etiquetas de las clases en el gráfico
plt.show() #Se muestra el gráfico con el nuevo punto y los puntos de las clases A y B

distanciasClaseA = list() #Se crea la lista para almacenar las distancias euclidianas que hay del punto generado hacia los puntos de la clase A
distanciasClaseB = list() #Se crea la lista para almacenar las distancias euclidianas que hay del punto generado hacia los puntos de la clase B

"""Se calculan las distancias euclidianas entre el punto generado y los puntos de la clase A, los resultados se agregan a 
la lista de distancias de la clase A"""
for i in range(0,10):
 distanciasClaseA.append(math.dist(nuevo_punto, [clase1[:,0][i],clase1[:,1][i]])) 

"""Se calculan las distancias euclidianas entre el punto generado y los puntos de la clase B, los resultados se agregan a 
la lista de distancias de la clase B"""
for j in range(0,10):
  distanciasClaseB.append(math.dist(nuevo_punto, [clase2[:,0][j],clase2[:,1][j]]))
    
distanciasTotales = dict() #Se crea un diccionario para relacionar las distancias obtenidas con su clase correspondiente

distanciasTotales['A'] = distanciasClaseA #Se asignan las distancias de la clase A al diccionario
distanciasTotales['B'] = distanciasClaseB #Se asignan las distancias de la clase B al diccionario

print(f'\nDistancias correspondientes a cada clase: {distanciasTotales} \n') 

listaDistancias = distanciasClaseA + distanciasClaseB #Se crea una lista con todas las distancias calculadas (tanto de la clase A y B)
listaDistancias.sort() #Se ordenan todas las distancias obtenidas de menor a mayor
print(f'Total de distancias de menor a mayor: {listaDistancias} \n')

"""Mediante la función obtenerClase se recibe como parámetro el valor de k para hallar a los vecinos más cercanos, a su vez se va
registrando la clase de cada punto cercano para lograr identificar la clase a la que pertenece el punto generado de acuerdo a la
clase mayoritaria de puntos cercanos"""
def obtenerClase(k):
    contadorA = 0 #Se inicia el contador de vecinos de la clase A
    contadorB = 0 #Se inicia el contador de vecinos de la clase B
    for i in range (0,k):
        valor = listaDistancias[i] #Se obtiene la distancia del vecino k a analizar
        print(f'Distancia {[i+1]}: {valor}') 
        if(valor in distanciasTotales['A']): #Determina si la distancia pertenece a la clase A
            print(' Clase: A')
            contadorA+=1
        elif(valor in distanciasTotales['B']): #Determina si la distancia pertenece a la clase B
            print(' Clase: B')
            contadorB+=1
    """Determina la clase a la que pertenece el punto generado, a partir del recuento de todas las distancias evaluadas para cada clase"""        
    if (contadorA > contadorB): #Si la clase mayoritaria es A, entonces el dato pertenece a la clase A
        print('El valor pertenece a la clase A')
    elif(contadorB > contadorA): #Si la clase mayoritaria es B, entonces el dato pertenece a la clase B
        print('El valor pertenece a la clase B')
    elif(contadorB == contadorA): #Si se obtuvieron la misma cantidad de vecinos de cada clase, se asigna el dato a ambas clases
        print('El valor pertenece a la clase A y B')

for v in range(0,2):
    k = int(input("Ingresa el valor de k: ")) #Se ingresa el valor de k para calcular a los vecinos más cercanos
    obtenerClase(k) #Se invoca a la función para determinar la clase a partir del valor de k vecinos más cercanos
