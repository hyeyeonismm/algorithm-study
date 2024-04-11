def solution(dots):
    dots.sort()
    garo = abs(dots[0][0]-dots[2][0])
    dots.sort(key=lambda x : x[1])
    sero = abs(dots[0][1]-dots[2][1])
    return garo * sero