s = int(input())
sum = 1
count=1

while sum < s: #200보다 작을때 
    count+=1 
    sum+=count 

if sum == s:
    print(count)
else:
    print(count-1)