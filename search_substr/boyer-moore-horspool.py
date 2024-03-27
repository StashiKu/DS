# O(m*n)

def preprocess(sub, start, end):
    alphabet_table = [len(sub) for i in range(end - start + 1)]
    print(alphabet_table, 'al table')

    for i in range(len(sub) - 1):
        alphabet_table[ord(sub[i]) - start] = len(sub) - i - 1

    return alphabet_table

def bmh_search(text, sub):
    if (len(sub) > len(text)):
        return None
    i = len(sub) - 1
    n = i
    start_index = ord(" ")
    end_index = ord("~")

    print(start_index, end_index, 'end', '<<<<<<<<')
    alphabet_table = preprocess(sub, start_index, end_index)

    while i < len(text):
        if text[i-n:i + 1] == sub:
            return i - n
        i = i + alphabet_table[ord(text[i]) - start_index]

    return None

substring = 'apple'
text = 'awersome apple'
# print(bmh_search(text, substring))


def first(sub, start, end):
    # alph_table = [len(sub) for i in range(end - start)]
    #
    # for i in range(len(sub) - 1):
    #     alph_table[ord(sub[i]) - start] = len(sub) - i - 1
    #
    # return alph_table

    alpha_table = [len(sub) for i in range(end - start)]

    for i in range(len(sub) - 1):
        alpha_table[ord(sub[i]) - start] = len(sub) - i - 1

    return alpha_table


def bhm_test(text, sub):
    # if len(text) < len(sub):
    #     return None
    #
    # i = len(sub) - 1
    # n = i
    # start = ord(" ")
    # end = ord("~")
    # alph_table = first(sub, start, end)
    #
    # while i < len(text):
    #     if text[i-n:i+1] == sub:
    #         return i - n
    #
    #     i = i + alph_table[ord(text[i]) - start]
    #
    # return None
    if len(sub) > len(text):
        return None
    i = len(sub) - 1
    n = i
    start = ord(" ")
    end = ord("~")
    alpha_table = first(sub, start, end)

    while i < len(text):
        if text[i-n:i + 1] == sub:
            return i - n

        i = i + alpha_table[ord(text[i]) - start]

    return None

print(bhm_test(text, substring))

# txt = ABABABAD
#         ^j 1
# sub = ABC
#       ^
# [A:4, B:5, C:6, D:7]
# i = 2
# j = -1

