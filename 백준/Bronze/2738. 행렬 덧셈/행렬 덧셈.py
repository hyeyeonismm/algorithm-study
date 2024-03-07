n, m = map(int, input().split())

a, b = [], []

for i in range(n):
    rows = list(map(int, input().split()))
    a.append(rows)

for j in range(n):
    rows = list(map(int, input().split()))
    b.append(rows)

for k in range(n):
    for l in range(m):
        print(a[k][l] + b[k][l], end=" ")
    print()
