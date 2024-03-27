sequence = [1, 4, 5, 6, 11, 7, 4, 6, 9]

# def modified_linear_search(seq, el):
#     seq.append(el)
#     i = 0
#
#     while seq[i] != el:
#         i += 1
#
#     seq.pop()
#
#     if i != len(seq):
#         return i
#
#     return -1

# 06.09.13
# def mod_lin_search(seq, el):
#     seq.append(el)
#
#     i = 0
#
#     while seq[i] != el:
#         i += 1
#
#     seq.pop(len(seq) - 1)
#
#     if i > len(seq) - 1:
#         return -1
#
#     return i
#
# print(mod_lin_search(sequence, 11))

# 07.09.13
# def lin_search_mod(seq, el):
#     seq.append(el)
#
#     i = 0
#
#     while i < len(seq) - 1:
#         if seq[i] == el:
#             return i
#         else:
#             i += 1
#
#
#     seq.pop(len(seq) - 1)
#
#     if i > len(seq) - 1:
#         return -1
#
#     return i
#
# print(lin_search_mod(sequence, 11))


# 11.09.23
# def lin_sch_mod(seq, el):
#     seq.append(el)
#     i = 0
#
#     while el != seq[i]:
#         i += 1
#
#     seq.pop(len(seq) - 1)
#
#     if i > (len(seq) - 1):
#         return -1
#
#     return i
#
#
# print(lin_sch_mod(sequence, 11))


# 12.09.23

# def linear_search(seq, el):
#     seq.append(el)
#     i = 0
#     while i < (len(seq) - 1):
#         if seq[i] != el:
#             i += 1
#
#     seq.pop(len(seq) - 1)
#
#     if i > (len(seq) - 1):
#         return -1
#
#     return i
#
#
# print(linear_search(sequence, 11))

# 13.09.23

def lin_search(seq, el):
    seq.append(el)
    n = len(seq)
    i = 0
    while seq[i] != el:
        i += 1

    seq.pop(n-1)

    if i > len(seq) - 1:
        print(i, len(seq) - 1)
        return -1

    return i

# print(lin_search(sequence, 111))

# 02.09.23

def l_s(seq, el):
    seq.append(el)
    n = len(seq)
    i = 0

    while seq[i] != el:
        i += 1

    seq.pop(len(seq) - 1)

    if i > len(seq):
        return -1

    return i

print(l_s(sequence, 11), 'the end')
