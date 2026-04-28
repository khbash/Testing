a = [76, 73, 69, 67, 42, 24]

for i in range(len(a) - 1):
    m = max(a[i:])
    ind = a.index(m, i)
    a[i], a[ind] = a[ind], a[i]

print(a)