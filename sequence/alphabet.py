n = int(input())
# создали словарь
dictLower = {}
# прошлись по кол-ву слов
for _ in range(n):
    s = input()
    sLower = s.lower()
    if sLower not in dictLower:
        dictLower[sLower] = set()
    dictLower[sLower].add(s)
text = input()
mistakes = 0