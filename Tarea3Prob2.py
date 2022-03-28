#Importación de bibliotecas
import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt

#Definicion de constantes
g=9.8
r_esp=287

def eqfunc(y,P):
    """
    Función que declara la función a resolver por solve_ivp
    :param y: Altitud en [m]. La variable que el módulo solve_ivp considera independiente
    :param P: Presión en [Pa]. La variable que el módulo solve_ivp considera dependiente
    :return: La función a resolver por el módulo solve_ivp
    """
    return -g*( (1/r_esp) * 200/(293*200 - y) *P)

P0=[101325]  #Valor inicial
y0=0  #nivel del mar, altitud 0
yf=3100 #altura final para resolver


#creación del arreglo de altitudes a evaluar
ejey=np.arange(y0,yf,step=100)

#Aproximación numérica de la presión atmoseférica
P_aprox = scipy.integrate.solve_ivp(derfunc, [y0, yf], P0,t_eval=ejey,method='RK45')


#Mostrar los resultados
print('Los valores de presión para el rango de 0-3000 m cada 100 m son:')
print(P_aprox)

#Graficar los resultados
plt.plot(P_aprox.t, P_aprox.y[0], 'g.-', label='Valor aproximado por RK45')
plt.xlabel('Y [m]')
plt.ylabel('P [Pa]')
plt.grid()
plt.legend(loc='upper left')
plt.show()