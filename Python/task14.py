import math
import numpy as np
import matplotlib.pyplot as plt

cos=math.cos
pi = math.pi
x=[]
txk=[]
xk=[]
fxk=[]
result_cj=[]

for i in range(-5, 6, 1):  # generating the list (cant use float for decomlas so the number is devided by 10 in the for loop)
    z = i/10
    x.append(z)

for i in range(4):
    xk_equation = cos(((2*i+1)/4)*(pi/2))
    xk.append(xk_equation)
for idx,val in enumerate(x):
    
    #function=cos(pi*x)
    fourth_order=8*(cos(pi*x[idx])**4)-(8*(cos(pi*x[idx])**2))+1
    txk.append(fourth_order)
    
    fxk_equation=cos(pi*x[idx])
    fxk.append(fxk_equation)
    cj_equation=((2/11)+(fxk_equation*fourth_order))
    result_cj.append(cj_equation)


print("This is fxl",fxk)
print("\n")
print("This is xk",xk)
print("\n")
print("This is xk", txk)
print("\n")
print("This is result", result_cj)


""" ave=0
for q in txk:
    ave=(ave+q)/idx
    

print(txk)
print(ave) """



