n = list(map(int, input().split()))

new_n = []

for i in range(len(n) - 2):
    if (n[i] > n[i+1] < n[i+2]) or (n[i] < n[i+1] > n[i+2]):
        new_n.append(1)
    else:
        new_n.append(0)

print(new_n)