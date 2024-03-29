def solution(myString, pat):
    num = len(myString)
    while num>0:
        if myString[:num].endswith(pat):
            return myString[:num]
        else:
            num-=1
    