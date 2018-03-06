import numpy as np
#from ../partie1/exo1 import *

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

    print("\n\n\n")
    print("Tests de la methode du gradient conjugué\n\n")
    x0 = np.zeros((2,1))
    A= np.array([[1, 0], [0,1]])
    b= np.array([[1],[42]])
    print("A=\n", A)
    print("\nExpected:\n", b)
    print("\nGot:\n", A.dot(conjugate_grad(A, b, x0)))
    print("---------------------------------------\n\n\n")

    x0 = np.zeros((3,1))
    
    A = np.array([[8,0,0],[0,5,0],[0,0,11]])
    b= np.array([[1],[42],[21]])
    print("A=\n", A)
    print("\nExpected:\n", b)
    print("\nGot:\n", A.dot(conjugate_grad(A, b, x0)))
    print("---------------------------------------\n\n\n")

    #matrice a diagonale dominante
    
    A = np.array([[10,2,3],[2,5,2],[3,2,25]])
    b= np.array([[-4],[8],[11.5]])
    print("A=\n", A)
    print("\nExpected:\n", b)
    print("\nGot:\n", A.dot(conjugate_grad(A, b, x0)))
    print("---------------------------------------\n\n\n")
    print("Fin des tests")
    return 0

test()

