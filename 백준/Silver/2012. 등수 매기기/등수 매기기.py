import sys

n = int(input())
rank = []
cnt=0
for i in range(n):
    rank.append(int(sys.stdin.readline()))

rank.sort()


for i in range(1,n+1):
     cnt+=abs(i-rank[i-1])

print(cnt)