def solution(numbers):
    num = ['zero','one','two','three','four','five','six','seven','eight','nine']

    for v,k in enumerate(num):
        if k in numbers:
            numbers = numbers.replace(k,str(v))
            
    return int(numbers)