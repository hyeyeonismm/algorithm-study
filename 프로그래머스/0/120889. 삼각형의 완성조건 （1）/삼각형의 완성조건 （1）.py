def solution(sides):
    sides.sort()
    if sides[2] < sum(sides[:2]):
        return 1
    else:
        return 2