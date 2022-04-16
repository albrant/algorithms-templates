def bubble_sort(number, source_array):
    for i in range(number - 1):
        for j in range(0, number-i-1):
            var1 = source_array[j] + source_array[j+1]
            var2 = source_array[j + 1] + source_array[j]
            if var1 < var2:
                source_array[j], source_array[j+1] = source_array[j+1], source_array[j]
    return source_array


def get_big_number(n, arr):
    arr = bubble_sort(n, arr)
    return ''.join(arr)


def read_input():
    n = int(input())
    arr = input().split()
    return n, arr


if __name__ == '__main__':
    n, arr = read_input()
    print(get_big_number(n, arr))
