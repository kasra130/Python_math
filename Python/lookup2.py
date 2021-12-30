import pandas as pd
import numpy as np
import math
from sympy import *
e = math.e

tvalue = []  # The values builfing tables
tindex = []  # The index (-1<x<2, 0.5)


def deriv():
    x = Symbol('x')
    y = ((x**2)*(e**(-0.5*x)))
    yprime = y.diff(x)
    print(yprime)
    return yprime


deriv()

for i in range(-10, 30, 5):  # generating the list (cant use float for decomlas so the number is devided by 10 in the for loop)
    x = i/10
    # apending the values (-1,-0.5,0..... to the index list)
    tindex.append(x)
    # Entering the e equation i wish to build the table on
    val = 1/(e**(0.5*x))
    tvalue.append(val)  # appending values to the value list
# not really used but nice to look at the table in pandas format
lookup_table = pd.DataFrame(tindex, tvalue)
#lookup_table.drop(lookup_table.index[0:0], inplace=True)
#df=lookup_table.iloc[1: , :]


result = []  # where the calculation results are stored when the lookupMethod function is used


def lookupMethod(x):
    separation_index = 0.5  # space
    separation_val = tvalue[3]  # The value of spaced index from table
    for idx, val in enumerate(tvalue):

        try:  # must as it panicks when the list jumps from 0
            equation1 = separation_val + ((tvalue[idx]-separation_val)/(
                tindex[idx]-separation_index))*(x-separation_index)  # PDF equation
            # Completing the equation as the x^2 portion was missing (table are only the "e^-0.5x" values)
            equation = ((-0.5*(x**2))*equation1)+((2*x)*equation1)
            result.append(equation)

        except:
            pass  # skip the error
    # for nice formatting to see which value belongs to what value of the table
    table2 = [tindex, result]
    print("for when x=0.5\n")
    for q, y in zip(*table2):  # printing both index and value
        print(q, y)
    print("\n")


lookupMethod(0.5)


def val2(x):  # fucntion for the "real" value
    eqq = -0.5*x**2/2.71828182845905**(0.5*x) + 2*x/2.71828182845905**(0.5*x)
    return eqq


print("real value is", str(val2(0.5)))


# -----------------------------------------------------------------------------------------------------------------------------------
