n = int(input())
a=[]
count=0

for i in range(n):
    a.append(list(map(int, input().split())))
    
a.sort(key=lambda x: (x[1], x[0]))
tmp=0

for i,j in a:
    if i>=tmp:
        tmp=j
        count+=1


print(count)
