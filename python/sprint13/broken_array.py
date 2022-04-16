# id-67435403
def broken_search(nums, target) -> int:
    left_border = 0
    right_border = len(nums) - 1
    while left_border <= right_border:
        middle = (left_border + right_border) // 2
        if nums[middle] == target:
            return middle
        if nums[left_border] <= nums[middle]:
            if nums[left_border] <= target < nums[middle]:
                right_border = middle - 1
            else:
                left_border = middle + 1
        else:
            if nums[middle] < target <= nums[right_border]:
                left_border = middle + 1
            else:
                right_border = middle - 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
