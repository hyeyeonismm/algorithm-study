def solution(myString, pat):
    myString=list(myString)
    answer=''
    for i in range(len(myString)):
        if myString[i]=='A':
            answer+='B'
        else:
            answer+='A'
    if pat in answer:
        return 1
    else:
        return 0