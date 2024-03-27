def rle_easy(s):
    curr = s[0]
    ans = []

    for i in range(len(s)):
        if s[i] != curr:
            ans.append(curr)
            curr = s[i]
    ans.append(curr)

    return ''.join(ans)

def rle(s):
    curr = s[0]
    ans = []
    count = 0

    for i in range(len(s)):
        if s[i] == curr:
            count += 1
        else:
            ans.append(curr+str(count))
            curr = s[i]
            count = 1

    if (count > 0):
        ans.append(curr+str(count))

    return ''.join(ans)

def rle_2(s):
    def pack(s, cnt):
        if cnt > 1:
            return s + str(cnt)
        return s

    lastsym = s[0]
    lastpos = 0
    ans = []

    for i in range(len(s)):
        if s[i] != lastsym:
            ans.append(pack(lastsym, lastpos))
            lastsym = s[i]
            lastpos = 1
        else:
            lastpos += 1

    ans.append(pack(lastsym, lastpos))

    return ''.join(ans)



print(rle('AZBBBBBBWWWWWWHHHHHab'))
