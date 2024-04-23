import sys

n = int(sys.stdin.readline())
back = 1
twoback = 0

if n == 0:
    print(0)
elif n == 1:
    print(1)

else:
    for i in range(2, n + 1):
        sum_v = twoback + back  # 0+1=1 #1+1 #1+2 #2+3
        twoback = back  # 1 #2
        back = sum_v  # 2 #3

    print(sum_v)