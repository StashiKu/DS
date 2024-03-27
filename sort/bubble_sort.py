sequence = [9, 0, 6, -2, 7, 2, 3]

# def bubble_sort(seq):
#     sorted_index = len(seq)
#
#     while True:
#         number_of_swap = 0
#
#         for i in range(0, sorted_index - 1):
#             if seq[i] > seq[i + 1]:
#                 seq[i], seq[i+1] = seq[i+1], seq[i]
#                 number_of_swap += 1
#
#         sorted_index -= 1
#         if number_of_swap == 0:
#             break
#
#     return seq
#
#
# print(bubble_sort(sequence))


# def bubble_sort(seq):
#     n = len(seq)
#
#     while True:
#         number_of_swap = 0
#
#         for i in range(0, n - 1):
#            if seq[i] > seq[i + 1]:
#                number_of_swap += 1
#                seq[i], seq[i + 1] = seq[i + 1], seq[i]
#
#         if number_of_swap == 0:
#             break
#
#         n -= 1
#
#     return seq
#
# print(bubble_sort(sequence))

# 08.09.13
# def bubble_sort(seq):
#     sorted_index = len(seq)
#
#     while True:
#         number_of_swaps = 0
#         for i in range(0, sorted_index - 1):
#             if seq[i] > seq[i + 1]:
#                 seq[i], seq[i + 1] = seq[i + 1], seq[i]
#                 number_of_swaps += 1
#
#         sorted_index -= 1
#
#         if number_of_swaps == 0:
#             break
#
#     return seq
#
# print(bubble_sort(sequence))

# 11.09.23
#
# def bubble_sort(seq):
#     sorted_index = len(seq) - 1
#
#     while True:
#         number_of_swaps = 0
#
#         for i in range(0, sorted_index):
#             if seq[i] > seq[i + 1]:
#                 seq[i], seq[i + 1] = seq[i + 1], seq[i]
#                 number_of_swaps += 1
#
#         if number_of_swaps == 0:
#             break
#
#         sorted_index -= 1
#
#     return seq

# print(bubble_sort(sequence))


# 12.09.23

# def bubble_sort(seq):
#     sorted_index = len(seq) - 1
#
#     while True:
#         number_of_swap = 0
#
#         for i in range(0, sorted_index):
#             if seq[i] > seq[i + 1]:
#                 seq[i], seq[i + 1] = seq[i + 1], seq[i]
#                 number_of_swap += 1
#
#         if number_of_swap == 0:
#             break
#
#         sorted_index -= 1
#
#     return seq
#
#
# print(bubble_sort(sequence))

# 13.09.23

# def bubble(seq):
#     sorted_index = len(seq)
#
#     while True:
#         number_of_swaps = 0
#
#         for i in range(0, sorted_index - 1):
#             if seq[i] > seq[i + 1]:
#                 seq[i], seq[i + 1] = seq[i + 1], seq[i]
#
#                 number_of_swaps += 1
#
#         if number_of_swaps == 0:
#             break
#
#         sorted_index -= 1
#
#     return seq
#
# print(bubble(sequence))

# 02.09.23

# def bubble(seq):
#     n = len(seq)
#
#     while True:
#         numbers_of_swap = 0
#
#         for i in range(0, n - 1):
#             if seq[i] > seq[i + 1]:
#                 seq[i], seq[i+1] = seq[i+1], seq[i]
#                 numbers_of_swap += 1
#
#         if numbers_of_swap == 0:
#             break
#
#         n -= 1
#
#     return seq
#
# print(bubble(sequence))

# 26.09.23

def bubble(seq):
    sorted_index = len(seq)

    while True:
        number_of_swap = 0
        for i in range(0, sorted_index - 1):

            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]

                number_of_swap += 1


        sorted_index -= 1

        if number_of_swap == 0:
            break

    return seq

print(bubble(sequence))


