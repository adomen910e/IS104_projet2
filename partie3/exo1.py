#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

#fabrique une matrice de taille (N*N)x(N*N) qui represente l'equation de la chaleur

def mat_chaleur(N):
    n = N*N
    A = np.zeros((n,n))
    for i in range(n):
        A[i,i] = -4
        if(i+1 < n):
            A[i+1, i] = 1
            A[i, i+1] = 1
        if(i+N < n):
            A[i+N, i] = 1
            A[i, i+N] = 1
    h = 1/(N+1)
    return A/(h*h)

#linearise une matrice en un vecteur colonne
def mat_linear(T):
    size = T.shape
    X = np.zeros((size[0] * size[1],1))
    for i in range(size[0]):
        for j in range(size[1]):
            X[i*size[1]+j,0] = T[i,j]
    return X

#donne l'état du système (carré) defini par T selon l'equation de la chaleur (pas très français)
def chaleur(T):
    size = T.shape
    if (size[0] != size[1]):
        return 1
    A = mat_chaleur(size[0])
    b = mat_linear(T)
    return A.dot(b)
        
A = np.array([[2,1],[3,5]])
print(A.shape)
print(mat_chaleur(1))
print(mat_chaleur(2))
print(mat_chaleur(3))
print(mat_linear(A))

