#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from math import sqrt
from exo1 import Cholesky 

def test():
    A = np.random.rand(3,3)
    A = A.dot(np.transpose(A))
    print(A)

    B = Cholesky(A)

    #C = Cholesky(A)

    D = np.transpose(np.linalg.inv(B)).dot(np.linalg.inv(B))

    condA = np.linalg.cond(A)
    cond = np.linalg.cond(D.dot(A))
    print(cond, condA)
    #assert(cond < condA)
    print(cond/condA)
