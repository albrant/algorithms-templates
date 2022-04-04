for x in range(100, 1000):
    a = x // 100
    b = (x//10)%10
    c = x % 10
    s1 = a + b
    s2 = b + c
    if s1 > s2:
        res = int(str(s1) + str(s2))
    else:
        res = int(str(s2) + str(s1))
    if res == 1512:
        print(x)