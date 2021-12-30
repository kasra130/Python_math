
from sympy import diff, sin, exp
from sympy import *
from sympy.abc import x, y
import math
facto = math.factorial
e=math.e

#eqa = (3*sin(2*x))
eqa=e**(-2*x)
deriv_order = []
deriv_order.append(eqa)
result = []
rez = []


real = 3*sin(2*((math.pi/6)))

print("Real value when pi/6 is ", real)


def tylor(xq, n):
    for i in range(1, n+1):
        primeit = diff(eqa, x, i)
        deriv_order.append(primeit)
    for idx, val in enumerate(deriv_order):
        equation = eqa.subs(x, xq) + \
            (deriv_order[idx].subs(x, xq)*(y**idx))/facto(idx)
        equation2 = eqa.subs(x, xq) + \
            (deriv_order[idx].subs(x, xq)*((math.pi/6)**idx))/facto(idx)
        # equation = eqa.subs(x, xq) + \(deriv_order[idx].subs(x, xq)/facto(idx))
        result.append(equation)
        rez.append(equation2)
        addition = 0
    for q in rez:
        addition = addition+q

    a_error = abs(addition-real)
    p_error = abs(a_error/real)*100

    print("Addition of the results when using n= "+str(n)+" is "+str(addition))
    print("Absolute error when using n="+str(n)+" is plus-minus "+str(a_error))
    print("Absolute error when using n="+str(n)+" is "+str(p_error)+"%")

    return result


#print("Using x=0, and n=1 taylor polynomials "+ str(tylor(0, 1)))   #Do not run them at them same time, as they bundle into the same list
#print("Using x=0, and n=3 taylor polynomials "+ str(tylor(0, 3)))
print("Using x=0, and n=5 taylor polynomials " + str(tylor(0, 5)))
