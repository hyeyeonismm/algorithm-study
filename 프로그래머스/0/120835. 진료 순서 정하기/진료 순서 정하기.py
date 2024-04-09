def solution(emergency):
    answer = sorted(emergency, reverse=True)
    # for i in range(len(answer)): 
    #     if emergency[i] in answer:
    #         emergency[i] = answer.index(emergency[i])+1
    # return emergency
    return [answer.index(i) + 1 for i in emergency]

