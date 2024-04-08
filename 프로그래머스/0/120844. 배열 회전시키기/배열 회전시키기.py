from collections import deque
def solution(numbers, direction):
    answer=[]
    dq = deque(numbers)
    if direction =='right':
        dq.rotate(1)
    else:
        dq.rotate(-1)
    for i in dq:
        answer.append(i)
    return answer
    