#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from math import sqrt


'''Calcul un élément diagonal de la matrice T'''
def elem_diago(A,T,i) :
    elem = A[i,i]
    for k in range(i):
        elem -= T[i,k]**2
    return sqrt(elem)



'''Calcul un élément du corps de la matrice T'''
def elem_corps(A,T,i,j) :
    elem = A[j,i]
    for k in range(j):
        elem -= T[j,k]*T[i,k]
    elem = elem / T[j,j]
    return elem



'''Mise en place de l'algorithme de Cholesky à partir d'une matrice A
        symétrique définie positive et renvoie la matrice T triangulaire
        inférieure de la décompostion A = T * transposé(T)'''
def Cholesky(A) :
    size = A.shape
    T = np.zeros(size)
    for i in range(size[0]):
        for j in range(i+1):
            if i == j :
                T[i,j] = elem_diago(A,T,i)
            else :
                T[i,j] =  elem_corps(A,T,i,j)
    return T

########################################################################
''' Cet algorithme à une complexité en théta(n**3) avec n la dimension
    de la matrice A symétrique définie positive'''
########################################################################


'''test l'algorithme de Cholesky'''
def test() :
    A=np.array([[1,1,1,1],[1,5,5,5],[1,5,14,14],[1,5,14,30]])
    T = Cholesky(A)
    T1 = np.transpose(T)
    print("La matrice initiale est :")
    print(A)
    print("\n")
    
    print("Les matrices de la décomposition de Cholesky sont :")
    print(T)
    print("\n")
    print("Et sa transposée et:")
    print(T1)
    print("\n")
    print("La multiplication de ces deux matrices donne :")
    print(T.dot(T1))
    print("\n")
    print("Donc on a bien T * Tt == A")
    print("\n")
    
    print("------------------------------------------------------\n")
    A = np.array([[1,0,0],[0,1,0],[0,0,1]])
    T = Cholesky(A)
    T1 = np.transpose(T)
    print("Les matrices de la décomposition de Cholesky sont :")
    print(T)
    print("\n")
    print("Et sa transposée et:")
    print(T1)
    print("\n")
    print("La multiplication de ces deux matrices donne :")
    print(T.dot(T1))
    print("\n")
    print("Donc on a bien T * Tt == A")
    print("\n")
    
    print("------------------------------------------------------\n")
    A = np.array([[1.,0.],[0.,2.]])
    T = Cholesky(A)
    T1 = np.transpose(T)
    print("Les matrices de la décomposition de Cholesky sont :")
    print(T)
    print("\n")
    print("Et sa transposée et:")
    print(T1)
    print("\n")
    print("La multiplication de ces deux matrices donne :")
    print(T.dot(T1))
    print("\n")
    print("Donc on a bien T * Tt == A")
    print("\n")
    
    print("------------------------------------------------------\n")
    print("EXIT_SUCCESS")

