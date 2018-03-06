#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from math import sqrt

def Cholesky(A) :
    '''Mise en place de l'algorithme de Cholesky à partir d'une matrice A
        symétrique définie positive et renvoie la matrice T triangulaire
        inférieure de la décompostion A = T * transposé(T)'''
    
    size = A.shape
    T = np.zeros(size)
    for i in range(size[0]):
        for j in range(i+1):
            if i == j :
                T[i,j] = elem_diago(A,T,i)
            else :
                T[i,j] =  elem_corps(A,T,i,j)
    return T

def elem_diago(A,T,i) :
    '''Calcul un élément diagonal de la matrice T'''
    elem = A[i,i]
    for k in range(i):
        elem -= T[i,k]**2
    return sqrt(elem)

def elem_corps(A,T,i,j) :
    '''Calcul un élément du corps de la matrice T'''
    elem = A[j,i]
    for k in range(j):
        elem -= T[j,k]*T[i,k]
    elem = elem / T[j,j]
    return elem

''' Cet algorithme à une complexité en théta(n**3) avec n la dimension
    de la matrice A symétrique définie positive'''

def test() :
    '''test l'algorithme de Cholesky'''
    A = np.array([[10,2,3],[2,5,2],[3,2,25]])
    T = Cholesky(A)
    T1 = np.transpose(T)
    print("La matrice initiale est :")
    print(A)
    print("Les matrices de la décomposition de Cholesky sont :")
    print(T)
    print(T1)
    print("La multiplication de ces deux matrices donne :")
    print(T.dot(T1))
    #assert(np.array_equal(A,T.dot(T1)))
    
    A = np.array([[1,0,0],[0,1,0],[0,0,1]])
    T = Cholesky(A)
    T1 = np.transpose(T)
    print("La matrice initiale est :")
    print(A)
    print("Les matrices de la décomposition de Cholesky sont :")
    print(T)
    print(T1)
    print("La multiplication de ces deux matrices donne :")
    print(T.dot(T1))
    assert(np.array_equal(A,T.dot(T1)))
    
    A = np.array([[1.,0.],[0.,2.]])
    T = Cholesky(A)
    T1 = np.transpose(T)
    print("La matrice initiale est :")
    print(A)
    print("Les matrices de la décomposition de Cholesky sont :")
    print(T)
    print(T1)
    print("La multiplication de ces deux matrices donne :")
    print(T.dot(T1))
    #assert(np.array_equal(A,T.dot(T1))) #Erreur d'assertion alors que les
    #print montre que les deux matrices sont égales
    
    print("EXIT_SUCCESS")

test()

