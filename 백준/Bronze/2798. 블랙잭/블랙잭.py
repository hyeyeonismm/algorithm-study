import sys

n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
res = 0
tmp = []

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if card[i] + card[j] + card[k] <= m:  # 5+6+7 <= 21
                tmp.append(card[i] + card[j] + card[k])

print(max(tmp))