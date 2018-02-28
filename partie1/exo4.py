#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from math import sqrt

'''Determine les valeurs de la matrice T en position (i,j) 
a partir des elements deja calcules et de A,
complexite theta(j) (avec j <= n la dimension de la matrice) donc theta(n)'''

'''le resultat differe legerement si element diagonal ou pas'''
def cholesky_calcul(A, T, i ,j):
	result = A[j,i]
	for k in range(j):
		result -= T[i, k]*T[j, k]
	if i != j:
		return (result)/T[j,j]
	return sqrt(result)
	
'''Mise en place de la factorisation incomplete de Cholesky, 

sa complexite reste de l'ordre de theta(n**3) dans le pire des cas, 
dans le meilleur des cas (A matrice diagonale) theta(n**2)

complexite dans tous les cas : theta((m+n)*n) avec :
     n : taille de la ligne/colonne de A
     m : nombre d'elements non nuls de A (m <= n**2)

meme dans un cas de matrice nulle, on doit regarder tous les elements de la martice (soit n**2)
'''
def incomplete_cholesky(A):
	size=A.shape
	T= np.zeros(size)
	for i in range(size[0]):
		for j in range(i+1):
			if A[i,j] != 0:
				T[i,j] = cholesky_calcul(A,T,i,j)
	return T


'''pas encore fait les tests, mais ça doit marcher avec les memes matrices que l'exo1'''
def test_incomplete() :
        '''test l'algorithme de Cholesky (version incomplete)'''
        A = np.array([[1,2,3],[2,5,2],[3,2,25]])
        print("Matrice A :")
        print(A)
        T = incomplete_cholesky(A)
        T1 = np.transpose(T)
        print("Matrice inversée par Cholesky :")
        print(T)
        assert(np.array_equal(A,T.dot(T1)))

        A = np.array([[1,0,0],[0,1,0],[0,0,1]])
        print("Matrice A :")
        print(A)
        T = incomplete_cholesky(A)
        T1 = np.transpose(T)
        print("Matrice inversée par Cholesky :")
        print(T)
        assert(np.array_equal(A,T.dot(T1)))

        A = np.array([[9,0,0],[0,256,0],[0,0,1024]])
        print("Matrice A :")
        print(A)
        T = incomplete_cholesky(A)
        T1 = np.transpose(T)
        print("Matrice inversée par Cholesky :")
        print(T)
        assert(np.array_equal(A,T.dot(T1)))

        A = np.array([[9,0,0],[0,11,-3],[0,-3,1024]])
        print("Matrice A :")
        print(A)
        T = incomplete_cholesky(A)
        T1 = np.transpose(T)
        print("Matrice inversée par Cholesky :")
        print(T)
        assert(np.array_equal(A,T.dot(T1)))

        print("tests de Cholesky version incomplète ok")
'''	
	A = np.array([[1.,0.],[0.,2.]])
	print(A)
	T = incomplete_cholesky(A)
	T1 = np.transpose(T)
	print(T)
	print(T1)
	print(T.dot(T1))
	assert(np.array_equal(A,T.dot(T1)))
'''




test_incomplete()
