n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))

res = 0

num_list.sort(reverse=True)

res += (num_list[0] * k )* (m//k)
res += num_list[1] * (m%k)
    

print(res)