def solution(spell, dic):
    for i in range(len(dic)): #5
        for j in spell: #3
            if j in dic[i]:
                dic[i] = dic[i].replace(j,'')
            else:
                dic[i]=j
                break
    print(dic)
    if '' in dic:
        return 1
    else:
        return 2