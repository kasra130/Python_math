
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
inverse = np.linalg.inv


def space(n):
    print("\n"*n)  # done mind this

# Similar setup as the picture in "http://aix1.uottawa.ca/~jkhoury/temp.htm" will be used
# a)


def four_internal_point(T1, T2, T3, T4):     # fun
    print("Part A: ")
    v1 = T1+T2
    v2 = T2+T3
    v3 = T1+T4
    v4 = T3+T4  # pattern of points in the center in 9 squares inside 1 square

    A = np.array([[4, -1, -1, 0], [-1, 4, 0, -1],
                 [-1, 0, 4, -1], [0, -1, -1, 4]])  # Array for the 4 equation (hardocoded)
    B = np.array([[v1], [v2], [v3], [v4]])   # B vector
    A_inv = inverse(A)
    ab = (np.matmul(A_inv, B))  # A^-1 *B
    print(B)  # check B matches with example
    return ab


print("for example :"+str(four_internal_point(25, 20, 20, 30)))  # an example


space(10)
################################################################


# b)


def twentyfour_internal_points(TT1, TT2, TT3, TT4):
    print("Now part b)\n")
    v1 = TT1+TT2
    v2 = TT2+TT3
    v3 = TT1+TT4
    v4 = TT3+TT4  # Similar but vital points are taken
    matrixA = np.zeros((25, 25), int)  # array size of eq
    np.fill_diagonal(matrixA, 4)  # fill the center diagonal with 4s
    tf = np.ones(24)  # fill with 1s(number of 1s)
    tw = np.ones(20)
    zero = np.zeros(1)
    np.fill_diagonal(matrixA[1:], - tf)  # fill upper digonal
    np.fill_diagonal(matrixA[:, 1:], -tf)  # fill lower diagonal
    np.fill_diagonal(matrixA[:, 5:], -tw)  # fill lower five down
    np.fill_diagonal(matrixA[5:], - tf)  # fill upper five up
    for i in range(4, 24, 5):  # The execption rows
        for z in range(5, 24, 5):  # The exception columbs
            matrixA[i][z] = 0  # exceptions filled with zero
            matrixA[z][i] = 0

    print("matrixA:")
    print(matrixA)  # check matrix A against example
    space(2)

    matrixB = np.zeros((25, 1), int)  # setup matrix similar way

    tt1 = (np.ones(1))*TT1
    tt2 = (np.ones(1))*TT2
    tt3 = (np.ones(1))*TT3
    tt4 = (np.ones(1))*TT4
    tt_x1 = (np.ones(1))*(v1)
    tt_x5 = (np.ones(1))*(v2)
    tt_x25 = (np.ones(1))*(v4)
    tt_x21 = (np.ones(1))*(v3)

    np.fill_diagonal(matrixB[:], tt_x1)
    np.fill_diagonal(matrixB[24:], tt_x25)
    np.fill_diagonal(matrixB[4:], tt_x5)
    np.fill_diagonal(matrixB[20:], tt_x21)
    for x in range(1, 4):
        np.fill_diagonal(matrixB[x:], tt2)
    for x in range(9, 20, 5):
        np.fill_diagonal(matrixB[x:], tt3)
    for x in range(21, 24):
        np.fill_diagonal(matrixB[x:], tt4)
    for x in range(5, 16, 5):
        np.fill_diagonal(matrixB[x:], tt1)
    print("matrixB:")
    print(matrixB)  # check matrix against example
    space(2)

    matrixA_invers = inverse(matrixA)
    matrixAB = (np.matmul(matrixA_invers, matrixB))  # A^-1*B

    print("matrixAB:")  # check the results of temps against example
    print(matrixAB)
    # Seeting x axis for varibale points (x1,x2..x25)
    garbage_collection = np.zeros((25, 1), int)
    for w in range(1, 26):

        garbage_collection[w:] = w

    z = matrixAB  # z axis (temp)
    y = matrixB  # y axis (B values temp points)
    q = garbage_collection   # varibale points
    fig = plt.figure()  # plot
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(q, y, z, zdir='z', c='red')
    ax.set_xlabel('Xn points from square')
    ax.set_ylabel('B vecotr')
    ax.set_zlabel('Tempreture of each point')
    ax.yaxis._axinfo['label']['space_factor'] = 3.0

    plt.show()

    return matrixAB


space(10)
################################################################


# c) DO NOT RUN FUNCTIONS AT THE SAME TIME !!!!! :DDD

# exact fassion just modifed for n
def ntimes_internal_points(n, TT1, TT2, TT3, TT4):
    v1 = TT1+TT2
    v2 = TT2+TT3
    v3 = TT1+TT4
    v4 = TT3+TT4
    matrixA = np.zeros((n, n), int)
    np.fill_diagonal(matrixA, 4)
    tf = np.ones(n-1)
    tw = np.ones(n-5)
    zero = np.zeros(1)
    np.fill_diagonal(matrixA[1:], - tf)
    np.fill_diagonal(matrixA[:, 1:], -tf)
    np.fill_diagonal(matrixA[:, 5:], -tw)
    np.fill_diagonal(matrixA[5:], - tf)
    for i in range(4, n-1, 5):
        for z in range(5, n-1, 5):
            matrixA[i][z] = 0
            matrixA[z][i] = 0

    print("matrixA:")
    print(matrixA)
    space(2)

    matrixB = np.zeros((n, 1), int)

    tt1 = (np.ones(1))*TT1
    tt2 = (np.ones(1))*TT2
    tt3 = (np.ones(1))*TT3
    tt4 = (np.ones(1))*TT4
    tt_x1 = (np.ones(1))*(v1)
    tt_x5 = (np.ones(1))*(v2)
    tt_x25 = (np.ones(1))*(v4)
    tt_x21 = (np.ones(1))*(v3)

    np.fill_diagonal(matrixB[:], tt_x1)
    np.fill_diagonal(matrixB[n:], tt_x25)
    np.fill_diagonal(matrixB[4:], tt_x5)
    np.fill_diagonal(matrixB[n-5:], tt_x21)
    for x in range(1, 4):
        np.fill_diagonal(matrixB[x:], tt2)
    for x in range(9, n-5, 5):
        np.fill_diagonal(matrixB[x:], tt3)
    for x in range(n-4, n-1):
        np.fill_diagonal(matrixB[x:], tt4)
    for x in range(5, n-8, 5):
        np.fill_diagonal(matrixB[x:], tt1)
    print("matrixB:")
    print(matrixB)
    space(2)

    matrixA_invers = inverse(matrixA)
    matrixAB = (np.matmul(matrixA_invers, matrixB))

    print("matrixAB:")
    print(matrixAB)
    garbage_collection = np.zeros((n, 1), int)
    for w in range(1, n+1):

        garbage_collection[w:] = w

    z = matrixAB
    y = matrixB
    q = garbage_collection

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(q, y, z, zdir='z', c='red')

    ax.set_xlabel('Xn points from square')

    ax.set_ylabel('B vecotr')
    ax.set_zlabel('Tempreture of each point')
    ax.yaxis._axinfo['label']['space_factor'] = 3.0

    #ax.scatter(np.arange(1,26,1000), matrixB, matrixAB, zdir='z', c='red')

    plt.show()

    return matrixAB

 # ->   RUN THESE       --->
 # TRYYY


# four_internal_points(25, 20, 20, 30)  # A
#twentyfour_internal_points(25, 20, 20, 30)   #B
#ntimes_internal_points(200, 25, 20, 20, 30)  # C
