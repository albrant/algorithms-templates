def F(n):
    if n < 3:
        return n+1
    if n % 2 == 0:
        return 1
        # return n + 2*F(n + 2)
    else:
        return F(n - 2) + n - 2

k = 0
for i in range(1, 222, 2):
    f = F(i)
    print(f)
    if 10**4 > f >= 10**2:
        k += 1
print(k)
