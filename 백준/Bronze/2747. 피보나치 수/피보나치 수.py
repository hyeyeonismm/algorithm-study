import sys

n = int(sys.stdin.readline())
twoback, back = 0, 1
for i in range(n):
    twoback, back = back, back + twoback

print(twoback)