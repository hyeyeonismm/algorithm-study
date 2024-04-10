def solution(my_string):
    my_string = list(map(str, my_string.split()))
    i=1
    answer = int(my_string[0])
    while i<len(my_string):
        if my_string[i]=='+':
            answer += int(my_string[i+1])
        else:
            answer -= int(my_string[i+1])
        i+=2

    return answer