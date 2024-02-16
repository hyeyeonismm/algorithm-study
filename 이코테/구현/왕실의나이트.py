# 행위치: 1~8
# 열위치: a~h

# a1에 있을 때 -> c2나 b3으로 이동 가능
# c2에 있을 때 -> e3, a3, d4, b4, e1, a1

knight = str(input()) #c2
count = 0

row = int(knight[1]) #1~8
col = ord(knight[0]) #97~104

# 경우의수
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (1, -2), (-1, 2), (-1, 2)]

for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]
    if next_row <1 or next_row >8 or next_col <97 or next_col > 104:
        continue
    else:
        count+=1

print(count)