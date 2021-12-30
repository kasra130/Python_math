import math
import numpy as np
#import scipy.integrate as integrate
#import scipy.special as special
import sympy as sp
import matplotlib.pyplot as plt

pi = math.pi
inverse = np.linalg.inv


def space(n):
    print("\n"*n)


######################START###################
# POLYNOMIALS
# a)
print("answer to question a is:\n")
equation = np.poly1d([6.0, 1.0, -4.0, 1.0])
print(equation)
roots_a = np.roots(equation)
print(f"first root x1={roots_a[0]:.3f}")
print(f"first root x2={roots_a[1]:.3f}")
print(f"first root x3={roots_a[2]:.3f}")


# ------------
space(5)
# ------
# b)
print("answer to question b is:\n")
deriv = np.polyder(equation)
print(deriv)
roots_deriv = np.roots(deriv)
print(f"first root x1={roots_deriv[0]:.3f}")
print(f"first root x2={roots_deriv[1]:.3f}")


# ------------
space(5)
# ------
# c)
print("answer to question c is the graph:\n")


def fun(x):
    return ((6*x**3)+(x**2)-(4*x)+1)


def deriv_d(d):
    return ((18*d**2)+(2*d)-4)


y_list = []
y_list_deriv = []
t_start = -1.1
t_end = 1.1
step = 0.1
t = np.arange(t_start, t_end, step)
for idx, val in enumerate(t):

    y_s = fun(t)
    y_d = deriv_d(t)
    y_list.append(y_s)
    y_list_deriv.append(y_d)

plt.axhline(y=0.5, color='r', linestyle='-', label="zero refrence")
plt.plot(t, y_s, label="orginal")
plt.plot(t, y_d, label="First derivative")
plt.legend()
plt.show()


# ------------
space(5)
# ------
# d)
print("answer to question d is:\n")
z = sp.symbols('z', real=True)
integrant = pi*(((6*z**3)+(z**2)-(4*z)+1)**2)
volume = sp.integrate(integrant, (z, 0.5, 1))
print(f"The volume between the largest roots around x-axis = {volume:0.3f}")


############################################################################################################

# START MATRICES AND LINEAR SYSTEMS############################33

print("##############################################################################################################")
# ------------
space(10)
print("MATRIX PORTION \n")
# ------
# a, Finfing a^-1
print("answer to question a is:\n")
a = np.array([[4.5, -2.3, 2.3], [2.3, 1.2, -4.2], [5.3, 2.7, 5.3]])
print("The inverse of the matrix A is :")
a_inverse = inverse(a)
print(a_inverse)


# ------------
space(5)
# ------
# b)
print("answer to question b is:\n")
b = np.array([[55, 21, 3], [4, 33, 2], [1, 2, 4]])
ab = (np.matmul(a, b))
print("Dot product of Matrices A and B (AB) is :")
print(ab)


# ------------
space(5)
# ------
# c)
print("answer to question c is:\n")
ba = (np.matmul(b, a))
print("AB is:")
print(ab)
print("BA is:")
print(ba)
compare = ab == ba
equal_arr = compare.all()
print("The answer to wether ab=ba, is " + str(equal_arr))


# ------------
space(5)
# ------
# d)
print("answer to question d is:\n")

ab_inverse = inverse(ab)
b_inverse = inverse(b)
clown = (np.matmul(b_inverse, a_inverse))
print(ab_inverse)
print(clown)
print("The answer to wether AB^-1=B^-1 A^-1, is True")


# ------------
space(5)
# ------
# e)
print("answer to question d is:\n")

# my_matrix=[[1,2,-2,1],[-2,3,4,-3],[1,6,0,-1],[1,9,0,-1]]
my_matrix = [[1, 1, -2, 1], [-2, 3, 4, -3], [1, 6, 0, -1], [1, 9, 0, -1]]
answers = [[2], [2], [1], [12]]
variables = np.linalg.solve(my_matrix, answers)
print("x="+str(variables[0])+"  and y="+str(variables[1]) +
      "  and z="+str(variables[2])+"    and w= "+str(variables[3]))
