# t/c = O(n2)
# s/c = O(1)

unsorted_list = [4, -1, -5, 0, 5, 8]
# unsorted_list = [-5, -1, 0, 4, 5, 8]
# i = 2
# min_index = 3
# j = 3

# def selection_sort(u_list):
#     # if len(u_list) <= 1:
#     #     return u_list
#
#     for i in range(0, len(u_list) - 1):
#         min_index = i
#
#         for j in range(i + 1, len(u_list)):
#             if u_list[j] < u_list[min_index]:
#                 min_index = j
#
#         if min_index != i:
#             temp = u_list[i]
#             u_list[i] = u_list[min_index]
#             u_list[min_index] = temp
#
#     return u_list
#
#
# print(selection_sort(unsorted_list))

# 07.09.13
# def selection_sort(seq):
#     for i in range(0, len(seq) - 1):
#         min_index = i
#         for j in range(i + 1, len(seq)):
#             if (seq[min_index] > seq[j]):
#                 min_index = j
#
#
#         if i != min_index:
#             seq[i], seq[min_index] = seq[min_index], seq[i]
#
#     return seq
#
# print(selection_sort(unsorted_list))

# 08.09.13

# def selection_sort(seq):
#
#     for i in range(0, len(seq) - 1):
#         min_index = 0
#
#         for j in range(0, len(seq)):  ___________________<============ error
#             if (seq[min_index] > seq[j]):
#
#                 min_index = j
#
#
#         if min_index != i:
#             seq[i], seq[min_index] = seq[min_index], seq[i]
#
#
#     return seq
#
#
# print(selection_sort(unsorted_list))

# 11.09.23
# def selection_sort(seq):
#     for i in range(0, len(seq) - 1):
#         min_index = i
#         for j in range(i + 1, len(seq)):
#             if seq[min_index] > seq[j]:
#                 # seq[min_index], seq[j] = seq[j], seq[min_index] ------------------===============error
#                 min_index = j
#
#         if min_index != i:
#             seq[min_index], seq[i] = seq[i], seq[min_index]
#
#     return seq
#
# print(selection_sort(unsorted_list))

# 12.09.23

# def s_b_c(seq):
#     sorted_index = len(seq)
#
#     for i in range(0, sorted_index - 1):
#         min_index = i
#         for j in range(i +1, sorted_index):
#
#             if seq[min_index] > seq[j]:
#                 min_index = j
#
#         if min_index != i:
#             seq[i], seq[min_index] = seq[min_index], seq[i]
#
#         return seq
#
# print(s_b_c(unsorted_list))

# 02.09.23

def sbc(seq):

    # for i in range(0, len(seq) - 1):
    #     min_index = i
    #
    #     for j in range(i + 1, len(seq)):
    #
    #         if seq[min_index] > seq[j]:
    #             min_index = j
    #
    #     if min_index != i:
    #         seq[i], seq[min_index] = seq[min_index], seq[i]
    #
    #     return seq

    for i in range(0, len(seq) - 1):
        min_index = i

        for j in range(i + 1, len(seq)):

            if seq[min_index] > seq[j]:
                min_index = j

        if min_index != i:
            seq[i], seq[min_index] = seq[min_index], seq[i]

        return seq

print(sbc(unsorted_list))
