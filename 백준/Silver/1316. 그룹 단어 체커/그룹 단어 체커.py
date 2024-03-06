n = int(input())
count = n

for i in range(n):
    word = input()
    exam_set = set()
    exam_set.add(word[0])
    
    for j in range(1,len(word)):
       # 앞의 알파벳이랑 연속적이면 ㄱㅊ, exam_set 안에 안들어있으면 ㄱㅊ
       if word[j] not in exam_set:
          exam_set.add(word[j])
       elif word[j]!=word[j-1] and word[j] in exam_set: 
          count-=1
          break
       else:
          continue  
          

print(count)