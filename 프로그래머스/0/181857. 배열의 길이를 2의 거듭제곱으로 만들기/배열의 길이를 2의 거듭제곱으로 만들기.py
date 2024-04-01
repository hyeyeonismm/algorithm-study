def solution(arr):
    answer = []
    answer += arr
    i=0
    while 2**i < len(arr): # 2 < 1
        i+=1 
    
    n = 2**i - len(arr) # 2 - 1 = 1
    while n>0:
        answer.append(0)
        n-=1
    return answer
