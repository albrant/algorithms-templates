def merge1(arr, lf, mid, rg):
    ans = []
    arr_left = arr[lf:mid]
    arr_right = arr[mid:rg]
    arr_left.reverse()
    arr_right.reverse()
    while len(arr_left) > 0 and len(arr_right) > 0:
        if arr_left[-1] <= arr_right[-1]:
            ans.append(arr_left.pop())
        else:
            ans.append(arr_right.pop())
    ans.extend(arr_left[::-1])
    ans.extend(arr_right[::-1])
    arr = ans
    return arr


def merge(alist, start, mid, end):
    left = alist[start:mid]
    right = alist[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            alist[k] = left[i]
            i = i + 1
        else:
            alist[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            alist[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            alist[k] = right[j]
            j = j + 1
            k = k + 1
    return alist


def merge_sort(arr, lf, rg):
    # print(arr, lf, rg)
    if lf+1 < rg:
        mid = (rg + lf) // 2
        merge_sort(arr, lf, mid)
        merge_sort(arr, mid, rg)
        merge(arr, lf, mid, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected

