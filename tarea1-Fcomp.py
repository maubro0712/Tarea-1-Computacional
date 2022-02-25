import numpy as np
import matplotlib.pyplot as plt

def velT(tiempo):
    vfinal=tiempo*(5*10**(-3))+ 0.5
    return vfinal


#Declaración de límites de integrción

a=0
b=100

#Puntos de división

N=int(input('Número de puntos: '))

#Declaración de variables

desp=0

pasotiempo=(b-a)/(N-1)  #determinación / discretización del paso en el tiempo
iContador=0 #contador de iteraciones
acc=0.5/b
tset=[]
xset=[]

while iContador <= 100:
    if iContador==0 or iContador==100:
        xset.append(desp)
        tset.append(iContador)
        desp += pasotiempo*0.5*velT(i)
        iContador += pasotiempo
    else:
        xset.append(desp)
        tset.append(i)
        desp=desp+velT(i)*pasotiempo
        iContador += pasotiempo

print(desp)

plt.plot(tset,xset)
plt.show()

"""
def Simpson(h,tiempo):
    if tiempo==0 or tiempo==100:
        suma=(h/3)*velT(tiempo)
        return suma
    else:
        if tiempo%2==0:
            suma=(2/3)*h*velT(tiempo)
            return suma
        else:
            suma=(4/3)*h*velT(tiempo)
            return suma


for j in range (a,N):
    xset.append(desp)
    tset.append(j)
    desp+=Simpson(pasotiempo,j)

print(desp)
plt.plot(tset,xset)
plt.show()
"""
def derivarx0(Func,dif,x0):
    DerF=(Func(x0+dif)-Func(x0-dif))/(2*dif)
    #print(DerF)
    return DerF


def NewtRhap(x0,Func,dif):
    print('F(x)= ', Func(x0), 'x= ', x0)
    if derivarx0(Func,dif,x0)==0:
        print('Fp=0 no hay correccion')
        return 0
    else:
        correccion=-1*(Func(x0))/(derivarx0(Func,dif,x0))
        #print(correccion)
        return correccion


def Pos(tiempo):
    return (tiempo**2)*0.5*0.01-5
max=int(input('Cant max de iteraciones: '))
x0=10

for k in range (0,max):
    if round(Pos(x0),3)==0.000:
        print('F(x)= ',Pos(x0))
        print('Listo, la raíz es: ',x0,'se dio en ',k,'iteraciones')
        break
    else:
        x0=x0+NewtRhap(x0,Pos,0.001)
        k+=1

