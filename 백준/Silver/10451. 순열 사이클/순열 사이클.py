import sys

# 테스트 케이스
t = int(sys.stdin.readline())  # 2
arr = [0]


# DFS 함수 정의
def dfs(v):
    if not visited[v]:
        visited[v] = True
    if not visited[arr[v]]:
        dfs(arr[v])


for i in range(t):
    n = int(sys.stdin.readline())  # 8
    arr[1:] = list(map(int, sys.stdin.readline().split()))
    visited = [0] * (n + 1)

    # 순열 사이클 개수 구하기
    count = 0
    for i in range(1, len(visited)):
        if visited[i] == False:
            count += 1
            dfs(i)

    print(count)
