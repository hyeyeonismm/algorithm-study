from collections import deque

n = int(input())

arr = deque(list(range(1, n + 1)))

while len(arr) > 1:
    arr.popleft()
    arr.rotate(-1)

print(arr[0])
