from collections import deque

def solution(A, B):
    for i in range(0,len(A)):
        answer = deque(A)
        answer.rotate(i)
        tmp = ''.join(answer)

        if tmp == B:
            return i
    else:
        return -1
    

            