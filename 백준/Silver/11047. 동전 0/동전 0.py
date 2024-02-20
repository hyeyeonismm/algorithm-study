n, k = map(int, input().split())
count = 0
coins = []
for i in range(n):
    coins.append(int(input()))

coins.reverse()

while k != 0:
    for coin in coins:
        if coin <= k:
            count+=k//coin
            k = k%coin

print(count)