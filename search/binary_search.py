sequence = [1, 5, 8, 10, 11, 12, 14, 15]

def bin_search(seq, el):
    # l = 0
    # r = len(seq) - 1
    #
    # while l <= r:
    #     m = (l + r)//2
    #     target = seq[m]
    #
    #     if target == el:
    #         return m
    #     if target > el:
    #         r = m - 1
    #     if target < el:
    #         l = m + 1
    #
    # return -1

    l = 0
    r = len(seq) - 1

    while l <= r:
        m = (l + r) // 2

        if seq[m] == el:
            return m
        if seq[m] < el:
            l = m + 1
        if seq[m] > el:
            r = m - 1

    return -1

print(bin_search(sequence, 12))
