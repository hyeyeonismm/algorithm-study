m, n = map(int, input().split())  # 3, 16
arr = [1] * (n + 1)
arr[0] = arr[1] = 0
# [1, 1, 1, 1, 1, ... ]
# [0, 1, 2, 3, 4, 5 ..., 16]
sqr = int(n**0.5)
for i in range(2, sqr + 1):  #  3 4
    j = 2
    while i * j <= n:
        arr[i * j] = 0
        j += 1

for idx, num in enumerate(arr):
    if num == 1 and idx >= m:
        print(idx)