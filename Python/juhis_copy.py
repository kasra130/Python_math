import math
import numpy as np
import matplotlib.pyplot as plt
#i do not understand this
facto=math.factorial
def horner(coeff,x):
    #horners rule here is used to eval polynomial at x and coeff is the ascending order of degrees
    accumulation=0
    for c in reversed(coeff):
        accumulation=accumulation*x+c
    return accumulation



def coeff(n):
    return [1/facto(i) for i in range(0,n)]


def help():
    for _ in range(20):

        print("\n")


trange1=np.arange(0,5.0,0.01)
trange2 = np.arange(0, 13.0, 0.01)
t1=horner(coeff(12),trange1)
t2 = horner(coeff(12), trange2)

print("this is triange1"+str(trange1))
help()
print("this is triange2"+str(trange2))
help()
print("this is t1"+str(t1))
help()
print("this is t2"+str(t2))



plt.subplot(211)
plt.plot(trange1,t1)
plt.plot(trange1,np.exp(trange1))
plt.grid()
plt.subplot(212)
plt.plot(trange2,t2)
plt.plot(trange2, np.exp(trange2))
plt.grid()
plt.legend(["n=11","exp(x)"])
plt.show()

