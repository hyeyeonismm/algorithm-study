n, k = map(int, input().split())
# 17 4
cnt = 0

# n이 커질수록 비효율적
# while n != 1:
#     cnt += 1
#     if (n % k ==0):
#         n /= k
#     else:
#         n -= 1

while True:
    # n이 k로 나누어 떨어지는 수가 될 때까지 1씩 빼기
    tmp = (n // k) * k
    cnt += (n - tmp)
    n = tmp

    # n이 k보다 작을 때 반복문 탈출
    if n < k:
        break
    cnt += 1
    n //= k

cnt += (n - 1)
print(cnt)