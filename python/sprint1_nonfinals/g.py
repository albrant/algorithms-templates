def to_binary(number: int) -> str:
    answer = ''
    while number > 0:
        answer = str(number % 2) + answer
        number //= 2
    return answer


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
