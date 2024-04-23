import sys

n = int(sys.stdin.readline())


def fib(num):
    if num == 0:
        return 0
    if num <= 2:
        return 1
    return fib(num - 2) + fib(num - 1)


print(fib(n))