import numpy as np

def mat(x,y):
    a = np.zeros((x,y))
    
    for i in range(x):
        l = [int(i) for i in input().split()]
        
        for j in range(y):
            a[i,j] = l[j]
    
    return a



