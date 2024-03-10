import math

n, k = map(int, input().split())  # 16, 2
arr = [[0 for j in range(k)] for i in range(1, 7)]
cnt = 0

for i in range(n):
    tmp = list(map(int, input().split()))  # [1,1]
    arr[tmp[1] - 1][tmp[0]] += 1

for i in range(len(arr)):
    for j in range(2):
        if arr[i][j] > 0 and arr[i][j] <= k:
            cnt += 1
        elif arr[i][j] > k:
            cnt = cnt + math.ceil(arr[i][j] / k)

print(cnt)
