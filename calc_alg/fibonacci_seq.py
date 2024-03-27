mem = dict()

def fibonacci_seq(n):
    if n in mem:
        return mem[n]

    if n == 1:
        mem[n] = 1
    elif n == 0:
        mem[n] = 0
    else:
        mem[n] = fibonacci_seq(n-1) + fibonacci_seq(n-2)
    return mem[n]
