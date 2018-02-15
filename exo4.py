#!/usr/bin/python3.2
# -*- coding: Utf-8 -*-

import numpy as np

a= np.matrix('1 2; 3 4; 1 2')
print(a.T)

def cholesky_calcul(A, T, i ,j):
	if i != j:
		S = 0
		for k in range(i):
			S += T[i, k]*T[j, k]
		return (A[i,j] - S)/T[i,i]
	else:
		S = 0
		for k in range(i):
			S += T[i,k]*T[i,k]
		return A[i,i] - S
	

def incomplete_cholesky(A):
	size=A.shape
	T=np.zeros(size)
	n = size[0]
	if n != size[1]:
		return 0
	for i in range(n):
		for j in range(n):
			if A[i,j] != 0:
				T[i,j] = cholesky_calcul(A,T,i,j)
	return 0

print(incomplete_cholesky(a))

print("hello world")
