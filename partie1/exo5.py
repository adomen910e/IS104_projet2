#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from exo1 import Cholesky
from exo4 import incomplete_cholesky

def test():
    A = np.random.rand(3,3)
    A = A.dot(np.transpose(A)) # On génère une matrice symétrique définie positive
    print("Notre matrice symétrique définie positive :")
    print(A)
    
    B = Cholesky(A)
    
    C = incomplete_cholesky(A)
    
    D = np.transpose(np.linalg.inv(B)).dot(np.linalg.inv(B))
    
    E = np.transpose(np.linalg.inv(C)).dot(np.linalg.inv(C))
    
    condA = np.linalg.cond(A)
    cond1 = np.linalg.cond(D.dot(A))
    cond2 = np.linalg.cond(E.dot(A))
    print("Le conditionnenment de M-1 . A avec la première méthode :", cond1,"Le conditionnenment avec la deuxième méthode :", cond2, "cond(A)", condA)
    print("\n")
    print("Rapport entre le premier conditionnement et cond(A)", cond1/condA,"Rapport entre le second conditionnement et cond(A)", cond2/condA)
    print("\n")


