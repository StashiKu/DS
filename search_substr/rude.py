string = 'test bingo test_test_test bingo test test'
substring = 'bingo'

# def str_equal(text, sub, i):
#     return sub == text[i:i+len(sub)]
#
# def rude(text, sub):
#     result = []
#
#     for i in range(len(text) - len(sub)):
#         if str_equal(text, sub, i):
#             result.append(i)
#
#     return result
#
#
# print(rude(string, 'bingo'))


# 08.09.13
# def str_equal(text, sub, i):
#     return sub == text[i:len(sub) + i]
#
# def muscle(text,sub):
#     result = []
#
#     for i in range(len(text) - 1):
#         if str_equal(text, sub, i):
#             result.append(i)
#
#     return result
#
# print(muscle(string, 'bingo')


# 11.09.23
# def equal_str(text ,sub, i):
#     return sub == text[i:i + len(sub)]
#
# def rude(text, sub):
#     res = []
#     for i in range(0, len(text) - len(sub)):
#         if equal_str(text, sub, i):
#             res.append(i)
#
#     return res
#
# print(rude(string, 'bingo'))

# 12.09.23

# def eq_str(text, sub, i):
#     return sub == text[i, i + len(sub)] -------------------<============== error : instead of coma
#
# def rude(text, sub):
#     res = []
#     for i in range(0, len(text) - len(sub)):
#         if eq_str(text, sub, i):
#             res.append(i)
#
#     return res
#
# print(rude(string, 'bingo'))

# 13.09.23

# def equal_str(text, sub, i):
#     return sub == text[i:i + len(sub)]
#
# def rude(text, sub):
#     res = []
#
#     for i in range(0, len(text) - len(sub)):
#         if equal_str(text, sub, i):
#             res.append(i)
#
#     return res
#
# print(rude(string, substring))

# 02.09.23

def eq_str(text, sub, i):
    # return sub == text[i:i + len(sub)]

    return sub == text[i: i + len(sub)]

def rude(text, sub):
    # res = []
    #
    # for i in range(0, len(text) - len(sub)):
    #     if eq_str(text, sub, i):
    #         res.append(i)
    #
    # return res

    res = []

    for i in range(0, len(text) - len(sub)):
        if eq_str(text, sub, i):
            res.append(i)

    return res


print(rude(string, substring))

