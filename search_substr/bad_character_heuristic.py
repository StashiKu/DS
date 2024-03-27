# Python3 Program for Bad Character Heuristic
# of Boyer Moore String Matching Algorithm 

NO_OF_CHARS = 256


def bad_char_heuristic(string, size):
    # Initialize all occurrence as -1
    bad_char = [-1] * NO_OF_CHARS

    # Fill the actual value of last occurrence
    for i in range(size):
        bad_char[ord(string[i])] = i

    # return initialized list
    return bad_char


def search(txt, pat):
    m = len(pat)
    n = len(txt)

    # create the bad character list by calling
    # the preprocessing function bad_charHeuristic()
    # for given pattern

    bad_char = bad_char_heuristic(pat, m)

    # s is shift of the pattern with respect to text
    s = 0
    while s <= n - m:
        j = m - 1

        # Keep reducing index j of pattern while
        # characters of pattern and text are matching
        # at this shift s
        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1

        # If the pattern is present at current shift,
        # then index j will become -1 after the above loop
        if j < 0:
            print("Pattern occur at shift = {}".format(s))

            s += (m - bad_char[ord(txt[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - bad_char[ord(txt[s + j])])


# Driver program to test above function
def main():
    txt = "ABAAABCD"
    pat = "ABC"
    search(txt, pat)


if __name__ == '__main__':
    main()
