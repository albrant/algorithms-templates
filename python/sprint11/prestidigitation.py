# id успешной попытки - 66209401
from typing import Tuple


def get_counts(string, keys_count):
    answer = 0
    keys_count *= 2
    for _ in range(10):
        cifer_count = string.count(str(i))
        if keys_count >= cifer_count > 0:
            answer += 1
    return answer


def read_input() -> Tuple[str, int]:
    keys_count = int(input())
    string = ''
    for _ in range(4):
        string += input().strip()
    return string, keys_count


if __name__ == '__main__':
    string, k = read_input()
    print(get_counts(string, k))
