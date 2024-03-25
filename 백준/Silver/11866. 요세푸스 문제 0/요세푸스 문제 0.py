import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
res = []

dq = deque(range(1, n + 1))

while len(dq) > 0:
    dq.rotate(-(k - 1))
    res.append(dq.popleft())

print(str(res).replace("[", "<").replace("]", ">"))