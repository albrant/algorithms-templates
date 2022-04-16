def buble_sort(n, arr):
    count = 0
    for i in range(n - 1):
        flag = True
        for j in range(n - 1):
            if arr[j] > arr[j+1]:
                flag = False
                count += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if flag:
            if count == 0:
                print(*arr)
            return
        print(*arr)


def read_input():
    n = int(input())
    arr = list(map(int, input().split()))
    return n, arr


if __name__ == '__main__':
    n, arr = read_input()
    buble_sort(n, arr)
