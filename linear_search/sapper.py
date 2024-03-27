def make_field(n, m, mines):
    dx = (0, 0, 1, -1, 1, 1, -1, -1)
    dy = (-1, 1, 0, 0, -1, 1, 1, -1)

    fields = []

    for i in range(n + 2):
        fields.append([0] * (m + 2))

    for minei, minej in mines:
        for k in range(len(dx)):
            fields[minei + dx[k]][minej + dy[k]] += 1

    for minei, minej in mines:
        fields[minei][minej] = '*'

    return fields

mines = [[1,3], [2,1], [4,2], [4,4]]

res = make_field(4,4, mines)

for i in range(len(res)):
    print(res[i])
