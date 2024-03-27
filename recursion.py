# recursion
base_list = [1, [4, 5], 5, 7, 8, [[1, 4, 5], 5], 9, 19]
string = 'hello hello hello h h'


# def get_element(list_array, result_list=None):
#     if result_list == None:
#         result_list = []
#
#     for el in list_array:
#         if type(el) == list:
#             get_element(el, result_list)
#         else:
#             result_list.append(el)
#
#     return result_list
#
# print(get_element(base_list))


# def get_space_num(string):
#     if len(string) == 0:
#         return 0
#
#     n = 0
#
#     if string[0] == ' ':
#         n += 1
#
#     return n + get_space_num(string[1:])
#
#
# print(get_space_num('hel lo m y friends'))


# def rec_find_space(string):
#     if len(string) == 0:
#         return 0
#
#     n = 0
#
#     if string[0] == ' ':
#         n += 1
#
#     return n + rec_find_space(string[1:])
#
# print(rec_find_space('hel lo m y friends'))

# 08.09.13

# def flat_array(base_l, result_list=None):
#     if result_list == None:
#         result_list = []
#
#     for el in base_l:
#         if type(el) == list:
#             flat_array(el, result_list)
#         else:
#             result_list.append(el)
#
#
#     return result_list
#
# print(flat_array(base_list))

# def count_space(str):
#     n = 0
#
#     if len(str) == 0:
#         return 0
#
#     if str[0] == ' ':
#         n += 1
#
#     return n + count_space(str[1:])
#
# print(count_space('hello hello hello h h'))


# 11.09.23

# def flat(base_l, result_list=None):
#     if result_list == None:
#         result_list = []
#
#     for el in base_l:
#         if type(el) == list:
#             flat(el, result_list)
#         else:
#             result_list.append(el)
#
#     return result_list
#
# print(flat(base_list))

# def count_space(string):
#     if len(string) == 0:
#         return 0
#
#     n = 0
#
#     if string[0] == ' ':
#         n += 1
#
#
#
#     return n + count_space(string[1:])
#
# print(count_space('hello hello hello h h'))

# 12.09.23
# def flat(s_list, res_list=None):
#     if res_list == None:
#         res_list = []
#
#     for el in s_list:
#         if type(el) == list:
#             flat(el, res_list)
#         else:
#             res_list.append(el)
#
#     return res_list
#
# print(flat(base_list))
#
# def count_space(string):
#     if len(string) == 0:
#         return 0
#
#     n = 0
#
#     if string[0] == ' ':
#         n = 1
#
#     return n + count_space(string[1:])
#
# print(count_space('hello hello hello h h'))

# 03.10.23

# def flat(original, result=None):
#     if result == None:
#         result = []
#
#     for el in original:
#         if type(el) == list:
#             flat(el, result)
#         else:
#             result.append(el)
#
#     return result
#
# print(flat(base_list))

def count_space(string):
    if len(string) == 0:
        return 0

    n = 0

    if string[0] == ' ':
        n = 1

    return n + count_space(string[1:])

print(count_space('hello hello hello h h'))