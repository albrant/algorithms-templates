from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:
    lfn = len(first_number)
    lsn = len(second_number)
    differ = abs(lfn - lsn)
    if lfn > lsn:
        second_number = '0' * differ + second_number
    else:
        first_number = '0' * differ + first_number
    length = max(lfn, lsn)
    ans = ''
    p = 0
    for i in range(length):
        a = int(first_number[-i-1])
        b = int(second_number[-i-1])
        c = (a + b + p) % 2
        p = (a + b + p) // 2
        ans = str(c) + ans
    if p > 0:
        ans = str(p) + ans
    return ans


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
