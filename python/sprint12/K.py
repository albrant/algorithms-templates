def fib(n, k):
    x, y = 1, 1
    k = 10**k
    for _ in range(2, n+1):
        x, y = y % k, (x + y) % k
    return y


n, k = map(int, input().split())
print(fib(n, k))
