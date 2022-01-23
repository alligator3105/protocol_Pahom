m = [
    ["Hello", "World"],
    ["Brad", "came", "to", "dinner", "with", "us"],
    ["He", "loves", "takos"]
]

rules = ["LEFT", "RIGHT", "LEFT"]

limit = 18

new_m = []
new_m.append('*' * limit)

s = ''

for i in m:
    for j in i:
        if len(s) + len(j) < limit - 2:
            s = s + j + ' '
        else:
            if rules[m.index(i)] == "LEFT":
                s = '*' + s.rstrip().ljust(limit - 2, ' ') + '*'
            elif rules[m.index(i)] == "RIGHT":
                s = '*' + s.rstrip().rjust(limit - 2, ' ') + '*'

            new_m.append(s)

            s = j + ' '

    if rules[m.index(i)] == "LEFT":
        s = '*' + s.rstrip().ljust(limit - 2, ' ') + '*'
    elif rules[m.index(i)] == "RIGHT":
        s = '*' + s.rstrip().rjust(limit - 2, ' ') + '*'

    new_m.append(s)
    s = ''

new_m.append('*' * limit)

for i in new_m:
    print(i)
