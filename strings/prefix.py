def prefix_function(text):
    n = len(text)
    pi = [0] * n

    for i in range(1, n):
        j = pi[i-1]
        while j > 0 and text[j] != text[i]:
            j = pi[j - 1]

        if text[i] == text[j]:
            j += 1

        pi[i] = j

    return pi

text = 'avada dedavra'

print(prefix_function(text))
