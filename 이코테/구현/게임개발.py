n, m = map(int, input().split())

# 맵을 생성하여 0으로 초기화
d=[[0]*m for _ in range(n)]

# 현재 좌표 입력
a, b, direction = map(int, input().split())

d[a][b]=1 # 현재 좌표 방문 처리



# 전체 맵 정보
map_info = []
for i in range(n):
   map_info.append(list(map(int, input().split())))

# 북 동 남 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
   global direction
   direction -= 1
   if direction == -1:
      direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0

while True:
   # 왼쪽으로 회전
   turn_left()
   nx = a + dx[direction]
   ny = b + dy[direction]

   # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
   if d[nx][ny] == 0 and map_info[nx][ny]== 0: 
      d[nx][ny]=1
      a = nx
      b = ny
      count+=1
      turn_time=0
      continue
   # 회전한 이후 정면에 가보지않은 칸이 없거나 바다인 경우
   else:
      turn_time+=1
    
    # 네 방향 모두 갈 수 없는 경우
   if turn_time ==4:
      nx = a - dx[direction]
      ny = b - dy[direction]

      # 뒤로 갈 수 있다면 이동하기
      if map_info[nx][ny]==0:
         a=nx
         b=ny

      # 뒤가 바다인 경우
      else:
        break
      turn_time = 0

print(count)