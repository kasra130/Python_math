def expo(x, n):
    assert n > -1
    assert isinstance(n, int)
    r = 1

    for i in range(n):
        i += 1
        r *= x
    return r


print(expo(456, 10))


def expofast(x, n):
    assert n > -1
    assert isinstance(n, int)
    r = 1

    if n % 2 == 0:
        nr = int(n/2)
        for i in range(nr):
            i += 1
            r *= x
        r *= r
    else:
        nr = int((n-1)/2)
        for i in range(nr):
            i += 1
            r *= x
        r *= r
        r *= x

    return r


print(expofast(3, 2))
 