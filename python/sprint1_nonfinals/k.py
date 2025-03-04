from typing import List, Tuple


def get_sum(number_list: List[int], k: int) -> List[int]:
    ans = "".join(list(map(str, number_list)))
    ans = int(ans) + k
    ans = list(str(ans))
    return ans


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k


number_list, k = read_input()
print(" ".join(map(str, get_sum(number_list, k))))
