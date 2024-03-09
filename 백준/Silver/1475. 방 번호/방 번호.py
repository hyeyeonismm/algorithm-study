import math

n = input()
num = [0] * 10


for i in range(len(n)):
    if n[i] == "9":
        num[6] += 1
    else:
        num[int(n[i])] += 1
num[6] = math.ceil(num[6] / 2)
print(max(num))