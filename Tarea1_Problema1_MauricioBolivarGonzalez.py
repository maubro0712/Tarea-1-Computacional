import numpy as np
import matplotlib.pyplot as plt

def velT(tiempo):
  """
  Función que calcula la velocidad para un tiempo dado
  parametros: Tiempo - El tiempo en segundos que ha pasado desde t = 0 s.
  """
  vfinal=tiempo*(5*10**(-3))+ 0.5
  return vfinal


#Declaración de límites de integración

a=0
b=100

#Puntos de división

N=int(input('Número de puntos: '))

#Declaración de variables

desp=0   #Variable que almacenará el almacenamiento

pasotiempo=(b-a)/(N-1)  #determinación / discretización del paso en el tiempo
iContador=0 #contador de iteraciones
acc=0.5/b  # Determinación de la aceleración constante
tLista=[]
xLista=[]

#Loop que recorre la integral para cada paso del tiempo, calcula
#el valor de la integral en cada intervalo y lo agrega a la variable desp
#además agrega los valores del tiempo y el desplazamiento a listas para graficarlos posteriormente

while iContador <= 100:
    if iContador==0 or iContador==100:
        xLista.append(desp)
        tLista.append(iContador)
        desp += pasotiempo*0.5*velT(iContador)
        iContador += pasotiempo
    else:
        xLista.append(desp)
        tLista.append(iContador)
        desp = desp+velT(iContador)*pasotiempo
        iContador += pasotiempo

print(desp)

plt.plot(tLista,xLista)
plt.show()