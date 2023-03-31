import numpy as np
import math as mt

tab = [190, 110, 170, 200, 220]
grades = [45,56,75,65,44,67,21,90,79,67,58,65]


def standard(x):
    semi = 0
    sumed = 0
    
    print(np.std(x))
    
    for y in x:
        semi += y
    
    semiR = semi/len(x)
    
    for y in x:
        temp = (y - semiR)*(y - semiR)
        sumed += temp
    
    resR = sumed/semiR
    print(resR)
    

def percentile(x):
    percent = int(input("Podaj perecentyl : "))
    result = np.percentile(x,percent)
    
    return(result)
    
#print(percentile(grades))
#standard(tab)
