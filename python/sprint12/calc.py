# id = 66774159

from operator import mul, floordiv, add, sub
from typing import List


class StackIsEmptyPopError(Exception):
    pass


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item: int) -> None:
        self.__items.append(item)

    def pop(self) -> int:
        if len(self.__items) == 0:
            raise StackIsEmptyPopError
        else:
            return self.__items.pop()


def is_digit(num_str: str) -> bool:
    try:
        int(num_str)
        return True
    except ValueError:
        return False


def calculate(operands: List) -> int:
    operators = {
        '*': mul,
        '/': floordiv,
        '+': add,
        '-': sub
    }
    stack = Stack()
    for operand in operands:
        if is_digit(operand):
            stack.push(int(operand))
        else:
            try:
                b = stack.pop()
                a = stack.pop()
            except StackIsEmptyPopError:
                print('Не удалось изъять из стэка операнд. Стэк пуст.')
                print('Продолжение расчётов невозможно!')
                break
            stack.push(operators[operand](a, b))
    try:
        answer = stack.pop()
        return answer
    except StackIsEmptyPopError:
        print('Невозможно изъять из стэка ответ. Стэк пуст')
        return None


if __name__ == '__main__':
    operands = input().split()
    print(calculate(operands))
