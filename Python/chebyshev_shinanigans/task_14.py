
from numpy.lib import polynomial
import numpy as np
import cheby
import math
import matplotlib.pyplot as plt

cos = np.cos
pi = np.pi
e=np.e


# coefs=np.loadtxt('coefs.txt')
coefs = np.array([0.5, 0.50547, 0, -0.061348, 0, 0.01109])  # Juhani's coeffs
# Plotting the coeffits using garbs
P = np.polynomial.chebyshev.Chebyshev(coefs[0:6])

0
x = np.linspace(-3, 3, 1000)
#y = 8*(cos(pi*x)**4)-(8*(cos(pi*x)**2))+1
y=1/(1+e**-x)
plt.plot(x, y, 'k', label="Real")  # original
plt.plot(x, P(x), '-', label="Approximate")  # approximate
plt.plot(x, y-P(x), 'r+', label="error")

R = P.roots()
print("cheby equation")
print(P)
print("\n")
print("roots")
print(R)
print("\n")
print(x)
for r, u in zip(R, x):
    print(r, u)

plt.legend()
plt.show()
