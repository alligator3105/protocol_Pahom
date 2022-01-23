m = [
    [1, 2, 3, 2, 7],
    [4, 5, 6, 8, 1],
    [7, 8, 9, 4, 5]
]

N = len(m[0])

a = set()

res = []

start = 0

while start != (N - 2):

    for row in m:
        for x in range(start, start + 3):
            a.add(row[x])

    if len(a) == 9:
        res.append(True)
    else:
        res.append(False)

    start += 1

    a.clear()

print(res)