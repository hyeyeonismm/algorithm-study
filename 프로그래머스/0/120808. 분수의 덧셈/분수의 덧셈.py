import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    answer.append(numer1*denom2 + numer2*denom1)
    answer.append(denom1*denom2)
    tmp = math.gcd(answer[0],answer[1])
    
    if tmp ==1:
        return answer
    else:
        while math.gcd(answer[0],answer[1]) != 1:
            answer[0]//=tmp
            answer[1]//=tmp
    
    return answer