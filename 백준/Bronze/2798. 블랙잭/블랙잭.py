import sys

n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
res = 0

for i in range(n):
    for j in range(i + 1, n):
        min_v = m
        for k in range(j + 1, n):
            if card[i] + card[j] + card[k] <= m:  # 5+6+7 <= 21
                if min_v > (m - (card[i] + card[j] + card[k])):  # 21> 3
                    min_v = m - (card[i] + card[j] + card[k])
                    idx = card[i] + card[j] + card[k]
        if idx > res:
            res = idx
        if idx == m:
            res = idx
            break

print(res)
