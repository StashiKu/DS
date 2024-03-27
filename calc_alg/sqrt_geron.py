def sqrt(a, err):
    x0 = a
    x1 = 1/2*(x0+a/x0)
    d = abs(x1-x0)

    while d >= 2*err and d**2 >= 2*err:
        x0 = x1

        x1 = 1/2*(x0+a/x0)
        d = abs(x1 -x0)
    return x1

print(sqrt(25, 0.01))

def test(n, err):
    x0 = n
    x1 = 1/2 * (x0 + n/x0)
    d = abs(x1-x0)

    while d >= 2*err and d**2 >= 2*err:
        x0 = x1

        x1 = 1/2 * (x0 + n/x0)
        d = abs(x1 - x0)