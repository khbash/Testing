a = [76, 73, 69, 67, 42, 24]

for i in range(len(a)-1):
    m = mах(a[i:])
    ind = a.index(m)
    a[i], a[ind] = a[ind], a[i]
    print(a)

for i in range(0, len(a)-1):
    for j in range(0, len(a)-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)

