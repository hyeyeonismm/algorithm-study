import math

S = input()
count=0

for i in range(1, len(S)):
    if S[i-1]!=S[i]: 
        count+=1
        res = count/2
    
if count == 0:
    print(0)
else:
    print(math.ceil(res))