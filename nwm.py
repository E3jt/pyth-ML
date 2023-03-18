import random as ra
import numpy as nm
import scipy as sc
from scipy import stats
tab1 = []
tab2_1 = []
tab2_2 = []
tab3 = []

def fc1(): 
    for i in range(1,10):
        tab1.append(ra.randrange(0,15))
        
    print(tab1)
    print(nm.mean(tab1))
    
def fc2():
    for i in range(1,10):
        tab2_1.append(i)
    tab2_1.append(9)
    
    print(tab2_1)
    print(nm.median(tab2_1))

    for i in range(1,10):
        tab2_2.append(i)
    
    print(tab2_2)
    print(nm.median(tab2_2))

def fc3():
    for i in range(1,10):
        tab3.append(ra.randrange(0,5))
    
    print(tab3)
    print(stats.mode(tab3))
   
fc1()   
fc2() 
fc3()