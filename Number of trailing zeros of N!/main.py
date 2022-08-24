from math import log, floor

def Z(n,k):
    denominator = 5**k
    z = n/denominator
    return(floor(z))

def zeros(n):
    nzeros = 0
    if n >0 & isinstance(n, int):
        kmax = floor(log(n,5))

        for x in range(1,kmax+1):
            nzeros += Z(n,x)
    return(nzeros)