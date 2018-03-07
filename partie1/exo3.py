import numpy as np
from random import *
from math import *
import numpy.linalg as alg






def generer_matrice(n,p, borne):
    
    k=randint(0,n-1)
    l=randint(0,n-1)
    compteur=0        #compte le nbr de cases hors de la diagonale déjà remplies
    A=np.zeros((n,n))
    
    if p > n*(n-1):
        print("Veuillez rentrer une autre valeur de p" ) 
    else:
        for i in range(n):
            A[i][i]=random()                #on initialise la diagonle
        while ( k!=l and compteur  < p ):
            A[k][l]=random()
            k=randint(0,n-1)
            l=randint(0,n-1)
            
            compteur+=1 
    
    for j in range (n):             #on crée des matrices strictement dominantes
        for i in range (n):         #pour assurer l'inversibilité
            A[i][i]=A[i][i]+abs(A[i][j])
            
    return np.transpose(A) * A #pour assurer la symétrie
    
    
def test_postivite(A):
    
    L=alg.eigvals(A)
    for i in range(len(L)):
        if L[i] <= 0:
            return False
        
    return True
    
def test_inversibilite(A):
    
    if np.linalg.det(A) == 0:
        print("matrice non inversible deterinant nul")
        return False
    else:
        print("test_inversibilite ok " )
    return True
    


def test_est_definie_positive (A) :
    if  test_inversibilite(A)==True and test_postivite(A)==True :
        return True
    return False
    
    
    

    
    

        
        
        


A= generer_matrice(5,5,1000);
print(A)
print(np.linalg.det(A))
bool=True
bool=test_est_definie_positive(A)
print(bool)


    



