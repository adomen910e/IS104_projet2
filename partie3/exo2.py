#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

# Pour des matrices creuses
import scipy.sparse as sp
from scipy.sparse.linalg.dsolve import spsolve

# pour estimer le temps d'execution
from time import time

N = 100         # Nombre de points (dans chaque direction)
dx = 1./(N-1);

xx = np.linspace(0,1,N)
yy = np.linspace(0,1,N)



# Definition du  Laplacien 1D
data = [np.ones(N),-2*np.ones(N),np.ones(N)]   # Termes Diagonaux
offsets = np.array([-1,0,1])                   # leurs positions
LAP = sp.dia_matrix( (data,offsets), shape=(N,N))

NN = N*N

# Identité NxN
I1D = sp.eye(N,N)

# Laplacien 2D
LAP2 = sp.kron(LAP,I1D)+sp.kron(I1D,LAP)
#Décommenter selon ce que vous voulez faire.
#f2 = -np.ones(NN)*dx**2 # Pour un plateau chauffant faiblement sauf aux bords
f2 = np.zeros(NN) # Pour les deux suivants cette ligne doit être décommentée
f2[N*(N + 1)/2] = -100 # Pour un plateau chauffant fortement au centre: c'est la question 2
#f2[NN-100:NN] += -100 # Pour un plateau chauffant fortement au nord: c'est la question 3

t = time()
T = spsolve(LAP2,f2) #résolution du système linéaire
print('temps sparse=' ,time()-t)

# In order to compare with the full resolution
#LAP2full=LAP2.todense()
#t=time(); T2=np.linalg.solve(LAP2full,f2); print 'temps full=',time()-t

# Résultat
plt.pcolormesh(xx,yy,T.reshape(N,N), shading='flat')
plt.axis('image')
plt.show()
