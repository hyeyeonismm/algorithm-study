max_val = -1
col = 0
row = 0

for i in range(9):
    nums = list(map(int, input().split()))

    for j in range(9):
        if max_val < nums[j]:
            max_val = nums[j]
            row = i + 1
            col = j + 1


print(max_val)
print(row, col)
