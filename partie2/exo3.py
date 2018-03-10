#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def conjugate_grad(A, b, x):
    r = b-np.dot(A, x)
    p = r
    r_k_norm = np.transpose(r).dot(r)

    for i in range(1,len(b)*10**3):
        Ap = A.dot(p)
        alpha = r_k_norm / np.transpose(p).dot(Ap)
        x += alpha * p
        r -= alpha * Ap
        r_kplus1_norm = np.transpose(r).dot(r)
        if r_kplus1_norm < 10**(-5):
            break
        p = r_kplus1_norm / r_k_norm * p + r
        r_k_norm = r_kplus1_norm
    return x

def test():
    print("\nTest de la methode du gradient conjugue\n")
    x0 = np.zeros((2,1))
    A= np.array([[1, 0], [0,1]])
    b= np.array([[1],[42]])
    print("A=")
    print(A)
    print("\nExpected:")
    print(b)
    print("\nGot:")
    print(A.dot(conjugate_grad(A, b, x0)))
    print("---------------------------------------\n")

    x0 = np.zeros((3,1))
    
    A = np.array([[8,0,0],[0,5,0],[0,0,11]])
    b= np.array([[1],[42],[21]])
    print("A=")
    print(A)
    print("\nExpected:")
    print(b)
    print("\nGot:")
    print(A.dot(conjugate_grad(A, b, x0)))
    print("---------------------------------------\n")

    #matrice a diagonale dominante
    
    A = np.array([[10,2,3],[2,5,2],[3,2,25]])
    b= np.array([[-4],[8],[11.5]])
    print("A=")
    print(A)
    print("\nExpected:")
    print(b)
    print("\nGot:")
    print(A.dot(conjugate_grad(A, b, x0)))
    print("---------------------------------------\n")
    print("Fin des tests")
    return 0

test()

