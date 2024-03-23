from collections import deque
import sys

n = int(sys.stdin.readline())
res = deque()

for i in range(n):
    order = sys.stdin.readline().split()
    if order[0] == "push":
        res.append(order[1])
    elif order[0] == "pop":
        if len(res) == 0:
            print(-1)
        else:
            print(res.popleft())

    elif order[0] == "size":
        print(len(res))

    elif order[0] == "empty":
        if len(res) == 0:
            print(1)
        else:
            print(0)

    elif order[0] == "front":
        if len(res) == 0:
            print(-1)
        else:
            print(res[0])

    elif order[0] == "back":
        if len(res) == 0:
            print(-1)
        else:
            print(res[-1])
