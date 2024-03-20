s = input()  # xy0z abaabba
p = input()  # zzz0yyy0xxx  aaabbbabbbaaa
count = 0
idx = 0

while idx < len(p):
    copy = ""
    if s.find(p[idx:]) != -1:
        count += 1
        break
    for j in range(idx, len(p)):
        copy += p[j]
        if s.find(copy) == -1:
            count += 1
            idx = j
            break

print(count)
