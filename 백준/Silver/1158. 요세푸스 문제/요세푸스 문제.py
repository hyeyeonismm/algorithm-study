from collections import deque

n, k = map(int, input().split())  # 7 3
arr = []
# 1 2 3 4 5 6 7
# 3 6 2 7 5 1 4

dq = deque()

for i in range(1, n + 1):
    dq.append(i)

while len(dq) != 0:
    dq.rotate(-(k - 1))
    arr.append(dq.popleft())


print(str(arr).replace("[", "<").replace("]", ">"))
