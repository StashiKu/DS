def merge(first_sequence, second_sequence):
    result = [0 for x in range(len(first_sequence) + len(second_sequence))]
    l = 0
    r = 0

    for i in range(len(result)):
        if l >= len(first_sequence):
            result[i] = second_sequence[r]
            r += 1
        elif r >= len(second_sequence):
            result[i] = first_sequence[l]
            l += 1
        elif first_sequence[l] < second_sequence[r]:
            result[i] = first_sequence[l]
            l += 1
        else:
            result[i] = second_sequence[r]
            r += 1

    return result

def mergeT(first, second):
    result = [0 for x in range(len(first) + len(second))]
    l = 0
    r = 0

    for i in range(let(range)):

first_sequence = [1, 3, 6, 9]
second_sequence = [2, 4, 4, 7]
result = merge(first_sequence, second_sequence)
print(result)