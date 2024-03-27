# 0(n + m)

def prefix_f(text):
    # n = len(text)
    # pi = [0] * n
    #
    # for i in range(1, n):
    #     j = pi[i - 1]
    #
    #     while j > 0 and text[i] != text[j]:
    #         j = pi[j - 1]
    #
    #     if text[i] == text[j]:
    #         j += 1
    #
    #     pi[i] = j
    #
    # return pi

    n = len(text)
    pi = [0] * n

    for i in range(0, len(text)):
        j = pi[i - 1]

        while j > 0 and text[i] != text[j]:
            j = pi[j - 1]

        if text[i] == text[j]:
            j += 1

        pi[i] = j

    return pi

def knut_morris_pratt(text, sub_text, index=0):
    # j = 0
    # pi = prefix_f(text)
    #
    # for i in range(index, len(text)):
    #     while j > 0 and text[i] != sub_text[j]:
    #         j = pi[j - 1]
    #
    #     if text[i] == sub_text[j]:
    #         j += 1
    #
    #     if j >= len(sub_text):
    #         return i - j + 1
    #
    # return None

    j = 0
    pi = prefix_f(text)

    for i in range(index, len(text)):
        while j > 0 and text[i] != sub_text[j]:
            j = pi[j - 1]

        if text[i] == sub_text[j]:
            j += 1

        if j >= len(sub_text):
            return i - j + 1

    return None

text_x = "AAATGAJACGDAACDDAATCTGT"
sub_text = "JACGDAACDDA"


print(knut_morris_pratt(text_x, sub_text))


