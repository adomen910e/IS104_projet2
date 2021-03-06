#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from math import sqrt
import exo1_1

def grad_conj_prec(A, b):
        '''implemente la methode du gradient conjugue avec preconditionneur'''
        x = np.zeros(b.shape)
        r = b - A.dot(x)
        B = exo1_1.Cholesky(A)
        m = np.linalg.inv(B.dot(np.transpose(B)))
        
        z = m.dot(r)
        p = z
        k = 0
        while sqrt(np.transpose(r).dot(r)) > 1 and 4*len(b) > k :
            a = (np.transpose(r).dot(z))/(np.transpose(p).dot(A.dot(p)))
            x = x + a*p
            r2 = r - a*(A.dot(p))
            z2 = m.dot(r)
            beta = (np.transpose(z2).dot(r2))/(np.transpose(z).dot(r))
            p = z2 + beta*p
            k += 1
            z = z2
            r = r2
            print(k)
        return x

def test() :
        '''test la methode du gradient conjugue avec preconditionneur'''
        A = np.array([[10,2,3],[2,5,2],[3,2,25]])
        b = np.array([[3],[6],[13]])
        x = grad_conj_prec(A, b)
        print("La matrice initiale est :")
        print(A)
        print("\n")
        print("la solution est :")
        print(x)
        print("\n")
        print("le second membre est :")
        print(b)
        print("\n")
        print("La multiplication de ces deux matrices donne :")
        print(A.dot(x))
        print("\n------------------------------------------------")
        
        A = np.array([[1,0,0],[0,1,0],[0,0,1]])
        b = np.array([[2],[5],[17]])
        x = grad_conj_prec(A, b)
        print("La matrice initiale est :")
        print(A)
        print("\n")
        print("la solution est :")
        print(x)
        print("\n")
        print("le second membre est :")
        print(b)
        print("\n")
        print("La multiplication de ces deux matrices donne :")
        print(A.dot(x))
        print("\n------------------------------------------------")
        
        
        A = np.array([[1.,0.],[0.,2.]])
        b = np.array([[7],[19]])
        x = grad_conj_prec(A, b)
        print("La matrice initiale est :")
        print(A)
        print("\n")
        print("la solution est :")
        print(x)
        print("\n")
        print("le second membre est :")
        print(b)
        print("\n")
        print("La multiplication de ces deux matrices donne :")
        print(A.dot(x))
        print("\n------------------------------------------------")
        print("EXIT_SUCCESS")

test()
