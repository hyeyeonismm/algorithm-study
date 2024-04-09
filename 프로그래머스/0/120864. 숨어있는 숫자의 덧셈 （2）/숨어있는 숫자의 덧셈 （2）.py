def solution(my_string):
    answer = 0
    tmp=''
    for i in my_string: #1
        if i.isdigit():
            tmp+=i ##1
        else:
            if tmp:
                answer+=int(tmp)
                tmp=''
    if tmp:
        answer+=int(tmp)
    
    return answer