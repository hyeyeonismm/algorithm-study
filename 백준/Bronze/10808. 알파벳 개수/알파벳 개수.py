s = input()

alph = [0] * 26

for i in range(len(s)):
    alph[ord(s[i]) - 97] += 1

for res in alph:
    print(res, end=" ")
