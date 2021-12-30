from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
inverse = np.linalg.inv
def space(n):
    print("\n"*n)
def twentyfour_internal_points(n, TT1, TT2, TT3, TT4):
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
    print(q)

    ser = [TT1, TT2, TT3, TT4]
    biggest = max(ser)

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


twentyfour_internal_points(200,25, 20, 20, 30)
