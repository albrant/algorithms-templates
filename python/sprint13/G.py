def count_sort(n, arr):
    temp = [0] * 3
    for elem in arr:
        temp[elem] += 1
    ans = []
    for i in range(len(temp)):
        ans.extend([i]*temp[i])
    return ans


n = int(input())
arr = [int(i) for i in input().split()]
print(*count_sort(n, arr))
