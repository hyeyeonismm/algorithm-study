def solution(before, after):
    after=list(after)
    for i in range(len(before)):
        if before[i] in after:            
            after.pop(after.index(before[i]))
            
    if len(after)==0:
        return 1
    else:
        return 0