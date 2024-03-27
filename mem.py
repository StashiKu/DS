# mem = dict()

# def mem_fac(num):
#     if num <= 1:
#         return 1
#     elif num in mem:
#         return mem[num]
#     else:
#         value = num * mem_fac(num - 1)
#         mem[num] = value
#
#         return value
#
# print(mem_fac(3))
# print(mem)



# def get_mem_func(fun):
    # mem = dict()
    #
    # def mem_fun(*arg):
    #     if arg in mem:
    #         print('in cash')
    #         return mem[arg]
    #     else:
    #         value = fun(*arg)
    #         mem[arg] = value
    #         return value
    # return mem_fun

# def factorial(n):
    # if n <= 1:
    #     return 1
    # else:
    #     return n*factorial(n-1)

# mem_func = get_mem_func(factorial)
# print(mem_func(3))

# 08.09.13

# def get_mem_func(fun):
#     mem = dict()
#
#     def mem_func(*arg):
#
#         if arg in mem:
#             return mem[arg]
#
#         else:
#             value = fun(*arg)
#             mem[arg] = value
#
#             return value
#
#     return mem_func
#
# def fact(n):
#     if n <= 0:
#         return 1
#
#     return n * fact(n-1)
#
# func = get_mem_func(fact)
#
# print(func(3))

# 11.09.23

# def get_mem_func(func):
#     mem = dict()
#
#     def mem_func(*arg):
#         if arg in mem:
#             return mem[arg]
#         else:
#             value = func(*arg)
#             mem[arg] = value
#
#             return value
#
#     return mem_func
#
# def fact(n):
#     if n < 1: -------------------<================= error
#         return 1
#
#     return n * fact(n - 1)
#
#
# func = get_mem_func(fact)
#
# print(func(4))

# 12.09.23

# def get_mem_func(fun):
#     mem = dict()
#
#     def mem_func(*arg):
#
#         if arg in mem:
#             return mem[arg]
#         else:
#             value = fun(*arg)
#             mem[arg] = value
#
#             return value
#
#     return mem_func
#
# def fact(n):
#     if n <= 1:
#         return 1
#
#     return n * fact(n - 1)
#
#
#
# func = get_mem_func(fact)
# print(func(3))

# 03.02.2023

def get_mem_func(func):
    mem = dict()

    def mem_func(*arg):
        if arg in mem:
            return mem[arg]
        else:
            value = func(*arg)
            mem[arg] = value

            return value

    return mem_func

def fact(n):
    if n <= 1:
        return 1

    return n * fact(n - 1)


func = get_mem_func(fact)
print(func(3))
