import math
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import sympy as sp
from sympy.abc import x, y



x = Function('x')
t = sp.symbols('t')


def f(x): return 3*sin(2*x)  # sp.exp, sp.sin


n = 4  # 3, 4, 5

deriv_list = [x(t), f(x(t))]  # list of derivatives [x(t), x'(t), x''(t),...]
for i in range(1, n):
    df_i = deriv_list[-1].diff(t).replace(sp.Derivative, lambda *args: f(x(t)))
    deriv_list.append(df_i)

#print("\n"+str(deriv_list)+"\n")




def der_xt(f, n):
    if n==1:
        return f(x(t))
    else:
        return der_xt(f,n-1).diff(t).replace(sp.Derivative,lambda *args: f(x(t)))

#print(der_xt(sp.sin,3))
""" #def deriv():
x = Symbol('x')
y = 3*sin(2*x)




def taylor(n):
    for i in range(n+1):
        yprime = y.diff(x,x)
 """


def diff(x_derivs_known, t, k, simplify=False):
    try:
        n = len(x_derivs_known)
    except TypeError:
        n = None
    if n is None:
        result = sp.diff(x_derivs_known, t, k)
        if simplify:
            result = result.simplify()
    elif k < n:
        result = x_derivs_known[k]
    else:
        i = n - 1
        result = x_derivs_known[i]
        while i < k:
            result = result.diff(t)
            j = len(x_derivs_known)
            x0 = None
            while j > 1:
                j -= 1
                result = result.subs(sp.Derivative(
                    x_derivs_known[0], t, j), x_derivs_known[j])
            i += 1
            if simplify:
                result = result.simplify()
    return result


print(diff((x(t), 3*sin(2*x(t))), t, 2, True))
for i in range(1, 4):
    print(diff(3*sin(2*x)), x, i)
