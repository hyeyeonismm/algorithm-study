def solution(numbers):
    num = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

    for v,k in enumerate(num):
        if k in numbers:
            numbers = numbers.replace(k,str(v))
            
    return int(numbers)