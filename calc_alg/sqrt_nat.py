def sqrt(number):
    l = 0
    r = number
    t = number

    while True:
        print(l, r, r//2)
        m = (l+r) // 2
        print(m, '<<<<')
        if m == t or m**2 == number:
            break
        if m**2 < number:
            l = m
        else:
            r = m
        t = m

    return m

print(sqrt(9.5))

