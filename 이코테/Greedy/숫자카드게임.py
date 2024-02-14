n, m = map(int, input().split())
res = 0
for i in range(n):
    num_list = list(map(int, input().split()))
    # num_list.sort()
    # if res < num_list[0]:
    #     res = num_list[0]

    # min을 사용하면 더 쉽게 풀 수 있음
    min_val = min(num_list)
    res = max(res, min_val)


print(res)