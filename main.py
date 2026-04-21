import random

def generate_files():
    sizes = [100, 300, 500, 1000, 1500, 2000]
    for n in sizes:
        data = sorted([random.randint(1, 1000) for _ in range(n)])
        with open(f'data_{n}.txt', 'w') as f:
            f.write(' '.join(map(str, data)))

generate_files()

a = []
for i in range(len(a)-1):
    m = mах(a[i:])
    ind = a.index(m)
    a[i], a[ind] = a[ind], a[i]
    print(a)