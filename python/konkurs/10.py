k = 0
for x in range(2**21, 2**22):
    binary = bin(x)
    if binary.find('111') == -1:
        k += 1
print(k)