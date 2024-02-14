import sys
import time
start_time = time.time() # 측정 시작


n = int(input())
rank = [0]*n
cnt=0
for i in range(n):
    rank[i] += (int(sys.stdin.readline()))

rank.sort()


for i in range(1,n+1):
     cnt+=abs(i-rank[i-1])

print(cnt)

end_time = time.time() # 측정 종료
print("time :", end_time - start_time) # 수행 시간 출력
