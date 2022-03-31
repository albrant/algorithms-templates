from typing import List


def transponed(matrix: List[list], width: int, height: int) -> List[list]:
    matrix2 = [([0] * height) for _ in range(width)]
    for i in range(height):
        for j in range(width):
            matrix2[j][i] = matrix[i][j]
    return matrix2


def read_matrix(width: int, height: int) -> List[list]:
    matrix = []
    for rows in range(height):
        row = list(map(int, input().strip().split()))
        matrix.append(row)
    return matrix


def print_matrix(matrix: List[list]):
    for rows in matrix:
        print(*rows)


if __name__ == "__main__":
    height = int(input())
    width = int(input())
    matrix = read_matrix(width, height)
    matrix = transponed(matrix, width, height)
    print_matrix(matrix)
