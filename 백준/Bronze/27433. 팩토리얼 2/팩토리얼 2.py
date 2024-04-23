import sys

n = int(sys.stdin.readline())
sum_v = 1

for i in range(1, n + 1):
    sum_v *= i

print(sum_v)