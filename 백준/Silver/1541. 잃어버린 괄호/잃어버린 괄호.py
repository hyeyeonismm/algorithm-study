num = input().split('-')


for i in range(len(num)):
   tmp=0
   if '+' in num[i]:
      num2 = num[i].split('+')
      for j in range(len(num2)):
         tmp+=int(num2[j])
      num[i]=tmp
   else:
      num[i]= int(num[i])

res=num[0]
for i in range(1, len(num)):
   res-=num[i]

print(res)
