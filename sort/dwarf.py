# time O(n)2
# memmory O(n)

sequence = [5, 0, -4, 8, 3, 4, 2]
# sequence = [-4, 0, 2, 3, 4, 5, 8]
# i = 6
# index = 7

# def dwarf_sort(seq):
#     i = 0
#     index = 1
#     n = len(seq)
#
#     while i < n - 1:
#         if seq[i] <= seq[i + 1]:
#             i, index = index, index + 1
#         else:
#             seq[i], seq[i + 1] = seq[i + 1], seq[i]
#             i = i - 1
#
#             if i < 0:
#                 i, index = index, index + 1
#
#     return sequence


# def dwarf_sort(seq):
#     i = 0
#     index = 1
#
#     while seq[i] < len(seq) - 1:
#
#         if seq[i] > seq[i + 1]:
#             seq[i], seq[i + 1] = seq[i + 1], seq[i]
#             i -= 1
#
#             if i < 0:
#                 i, index = index, index + 1
#
#         else:
#             i, index = index, index + 1
#
#
#     return seq
#
# print(dwarf_sort(sequence))

# def dwarf_sort(seq):
#     i = 0
#     index = 1
#
#     while i != len(seq) - 1:
#
#         if seq[i] > seq[i + 1]:
#             seq[i], seq[i + 1] = seq[i + 1], seq[i]
#             i -= 1
#
#             if i < 0:
#                 i, index = index, index + 1
#         else:
#             i, index = index, index + 1
#
#     return seq
#
# print(dwarf_sort(sequence))


# 08.09.13

# def dwarf(seq):
#     i = 0
#     index = 1
#     n = len(seq)
#
#     while i < n - 1:
#
#         if seq[i] > seq[i + 1]:
#             seq[i], seq[i + 1] = seq[i + 1], seq[i]
#             i -= 1
#
#             if i < 0:
#                 i, index = index, index + 1
#
#         else:
#             i, index = index, index + 1
#
#
#     return  seq
#
# print(dwarf(sequence))


# 11.09.23

# def dwarf_sort(seq):
#     i = 0
#     index = 1
#     n = len(seq)
#
#     while i < n - 1:
#         if seq[i] > seq[i + 1]:
#             seq[i], seq[i + 1] = seq[i + 1], seq[i]
#             i -= 1
#
#             if i < 0:
#                 i, index = index, index + 1
#
#         else:
#             i, index = index, index + 1
#
#     return seq
#
# print(dwarf_sort(sequence))


# 12.09.23

# def dwarf(seq):
#     i = 0
#     index = 1
#     n = len(seq)
#
#     while i < n - 1:
#         if seq[i] > seq[i + 1]:
#             seq[i], seq[i + 1] = seq[i + 1], seq[i]
#
#             i -= 1
#
#             if i < 0:
#                 i, index = index, index + 1
#
#         else:
#             i, index = index, index + 1
#
#     return seq
#
# print(dwarf(sequence))

# 02.09.23

def dwarf(seq):
    # i = 0
    # index = 1
    # n = len(seq)
    #
    # while i < n - 1:
    #     if seq[i] > seq[i + 1]:
    #         seq[i], seq[i + 1] = seq[i + 1], seq[i]
    #
    #         i -= 1
    #
    #         if i < 0:
    #             i, index = index, index + 1
    #
    #     else:
    #         i, index = index, index + 1
    #
    # return seq

    i = 0
    index = i
    l = len(seq)

    while i < l - 1:
        if seq[i] > seq[i + 1]:
            seq[i], seq[i + 1] = seq[i + 1], seq[i]

            i -= 1

            if i < 0:
                i, index = index, index + 1

        else:
            i, index = index, index + 1

    return seq

print(dwarf(sequence))
