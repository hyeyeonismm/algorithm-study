def solution(money):
    answer = []
    cnt = money//5500
    money = money%5500
    
    answer = [cnt, money]
    return answer