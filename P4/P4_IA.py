import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
import pandas as pd


fig,axes=plt.subplots() #Se define el gráfico a emplear

"""Se pasa el dataset a un dataframe para poder manipular mejor los atributos de las clases"""
datos = pd.read_csv('Museos.csv')
df = pd.DataFrame(datos)


"""Mediante el siguiente ciclo se realiza el proceso de estandarizacion de los valores con el fin de que se obtenga
una distribución gaussiana en donde la media de los valores sea igual a 0 y su varianza igual a 1 (este procedimiento es opcional)"""

for name in df.iloc[:, [2, 3, 4] ]:
    df[name] = (df[name]-df[name].mean())/df[name].std()


"""Se obtienen los valores de los 4 atributos del banco de datos y se guardan en un arreglo para cada atributo"""
a = df.iloc[:,2]
b = df.iloc[:,3]
c = df.iloc[:,4]

data = np.array([a, b, c]) #Se crea un arreglo que contenga los datos de todos los atributos

cov=np.cov(data) #Se obtiene la matriz de covarianza de los 4 atributos
print('Matriz de covarianza: \n', cov)

eig_vals, eig_vecs =np.linalg.eig(cov) #Con la matriz de covarianza se obtienen los valores y vectores propios en forma de matriz

print('Valores propios: \n', eig_vals) 
print('Vectores propios: \n', eig_vecs)

v_pc1 = eig_vecs[:,0] #Se obtienen los valores de la primera columna de la matriz de vectores propios
v_pc2 = eig_vecs[:,1] #Se obtienen los valores de la segunda columna de la matriz de vectores propios
print(v_pc1) 
print(v_pc2)

"""Se crean las listas para guardar los valores de las 2 componentes"""
pc1 = [] #Lista para la componente 1
pc2 = [] #Lista para la componente 2

"""Se separan los datos de cada clase para identificarlos en la gráfica con diferente color"""


"""Mediante el siguiente ciclo se multiplican los valores de cada atributo por los valores de las 2 
primeras columnas de vectores propios, generando así los valores para la componente 1 y 2"""
for i in range(32):
  pc1.append(v_pc1[0]*a[i]+v_pc1[1]*b[i]+v_pc1[2]*c[i])
  pc2.append(v_pc2[0]*a[i]+v_pc2[1]*b[i]+v_pc2[2]*c[i])

"""Finalmente se grafican los puntos con las 2 componentes generadas"""
for i in range(0,32):
        plt.scatter(-pc2[i], pc1[i], s = 15, c='b')

"""for i, etiqueta in enumerate(df['Entidad']):
    plt.annotate(etiqueta, (df['Mt'][i], df['Pt'][i]))"""

plt.xlabel('CP1')
plt.ylabel('CP2')

plt.show()