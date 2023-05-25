# -*- coding: utf-8 -*-
from numpy import *

from pylab import *

arch = open('solucion','w')

def f(x):
  k=2.
  return k*x

nPuntos=1000
t_i=0.
t_f=1.
dt=(t_f-t_i)/nPuntos

X=.3
T=t_i
print dt
print T
for i in range(0,nPuntos-1):
  T=T+dt
  X= X + f(X) * dt
  print T,X
  arch.write(str(T)+" "+str(X)+"\n")

plot(T,X)

show()
