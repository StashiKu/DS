iceland = [3, 1, 4, 3, 5, 1, 1, 3, 1]

def isleflood(h):
    maxpos = 0

    for i in range(len(h)):
        if h[i] > maxpos:
            maxpos = h[i]

    ans = 0
    nowm = 0

    for i in range(maxpos):
        if h[i] > nowm:
            nowm = h[i]

        ans += nowm - h[i]

    nowm = 0

    for i in range(len(h) - 1, maxpos, -1):
        if h[i] > nowm:
            nowm = h[i]

        ans += nowm - h[i]

    return ans
