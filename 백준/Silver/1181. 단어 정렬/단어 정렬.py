

n = int(input())
words=[]
for i in range(n):
    words.append(input()) 

words = list(set(words))
words.sort()
# len_words = sorted(words, key=len) 
words.sort(key=len)

   
for word in words:
    print(word)