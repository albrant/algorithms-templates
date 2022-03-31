# id успешной попытки - 66209886
from typing import List, Tuple


def get_distances(count: int, houses: List[int]) -> List[int]:
    answer = [0] * count
    current_position = 0
    while True:
        if houses[current_position] > 0:
            left_null_index = -10**7
        else:
            left_null_index = current_position
        try:
            right_null_index = houses.index(0, max(0, left_null_index)+1)
        except ValueError:
            right_null_index = 10**7
        for_to = min(right_null_index, count-1)
        for step in range(current_position, for_to + 1):
            answer[step] = min(right_null_index - step, step - left_null_index)
        current_position = for_to
        if current_position >= count-1:
            return answer


def read_input() -> Tuple[int, int]:
    count = int(input().strip())
    houses = [int(house_number) for house_number in input().strip().split()]
    return count, houses


if __name__ == '__main__':
    count, houses = read_input()
    print(" ".join(map(str, get_distances(count, houses))))
