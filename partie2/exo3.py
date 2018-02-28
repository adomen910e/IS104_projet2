import numpy as np

def conjugate_grad(A, b, x):
    r = b-np.dot(A, x)
    p = r
    r_k_norm = np.dot(r, r)

    for i in range(1,10**6):
        Ap = np.dot(A, p)
        alpha = r_k_norm / np.dot(p, Ap)
        x += alpha * p
        r -= alpha * Ap
        r_kplus1_norm = np.dot(r, r)
        beta = r_kplus1_norm / r_k_norm
        r_k_norm = r_kplus1_norm
        if r_kplus1_norm < 1e-5:
            print 'Itr:', i
            break
        p = beta * p + r
    return x
