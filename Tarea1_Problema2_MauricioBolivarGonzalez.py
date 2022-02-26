import numpy as np
import matplotlib.pyplot as plt


def derivarx0(Func,dif,x0):
  """
  Función que determina la derivada de una función en un punto x dado aproximandola
  mediante diferencias centradas con 1 punto a cada lado.
  Parámetros:
  -Func: Función a derivar
  -dif: Aproximación al concepto de un diferencial, variable tipo flotante
  -x0: Punto en el cuál se evaluará la derivada

  Return: DerF - una variable de tipo flotante que almacena el valor de la derivada evaluada en el punto x dado
  """
  DerF=(Func(x0+dif)-Func(x0-dif))/(2*dif)
  return DerF


def NewtRhap(x0,Func,dif):
  """
  Función que desarrolla el algoritmo de Newton-Raphson para encontrar raíces de
  una función de 1 sola variable. Además comprueba si existe o no una singularidad
  en la corrección a x.
  Parámetros:
  -x0: Punto inicial para comenzar el algoritmo
  -Func: Función cuya raíz se desea encontrar
  -dif: Aproximación al concepto de un diferencial, variable tipo flotante

  Return: Si la corrección no se puede calcular devuelve el valor de 0, caso contrario
  se devuelve la corrección (variable tipo flotante) a x.
  """
  print('F(x)= ', Func(x0), 'x= ', x0)
  if derivarx0(Func,dif,x0)==0:
        print('F-prima=0 no hay correccion')
        return 0
  else:
        correccion=-1*(Func(x0))/(derivarx0(Func,dif,x0))
        return correccion


def Pos(tiempo):
  """
Funcion que modela la posición con respecto al tiempo

Parámetro: tiempo - Tiempo en segundos desde que el objeto parte del reposo
return: la posición calculada como función del tiempo, como un float
  """
  return (tiempo**2)*0.5*0.01-5

#Declaración de variables y punto incial

max=int(input('Cant. max de iteraciones: '))
x0=1

for k in range (0,max):
    if round(Pos(x0),3)==0.000:
        print('F(x)= ',Pos(x0))
        print('Listo, la raíz es: ',x0,'se dio en ',k,'iteraciones')
        break
    else:
        x0=x0+NewtRhap(x0,Pos,0.001)
        k+=1