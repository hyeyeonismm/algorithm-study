def solution(dots):
    for i in range(len(dots)):
        x = dots[0][0]
        y = dots[0][1]
        if x==dots[i][0]:
            sero = abs(y-dots[i][1])
        if y==dots[i][1]:
            garo = abs(x-dots[i][0])
    return sero*garo