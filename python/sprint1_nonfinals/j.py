from typing import List


def factorize(number: int) -> List[int]:
    answer = []
    while number > 1:
        koren = int(number ** 0.5) + 2
        for i in range(2, koren):
            if number % i == 0:
                answer.append(i)
                number //= i
                break
        else:
            answer.append(number)
            return answer
    return answer


result = factorize(int(input()))
print(" ".join(map(str, result)))
