def binarySearch(arr, x, left, right):
    if right <= left:
        if right + 1 <= len(arr):
            return right + 1
        return -1
    mid = (left + right) // 2
    if x <= arr[mid]:
        return binarySearch(arr, x, left, mid)
    else:
        return binarySearch(arr, x, mid + 1, right)


def read_input():
    n = input()
    arr = list(map(int, input().split()))
    x = int(input())
    return arr, x


if __name__ == '__main__':
    arr, x = read_input()
    index = binarySearch(arr, x, left=0, right=len(arr))
    index2 = binarySearch(arr, 2*x, left=0, right=len(arr))
    print(index, index2)
