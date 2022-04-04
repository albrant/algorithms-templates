def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n

k = 0
s = 0
for i in range(1, 100):
    x = fac(i)
    if x <= 1000:
        k += 1
        s += x
        print(x)
print(k, s)
