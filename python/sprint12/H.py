# Дана скобочная последовательность.
# Нужно определить, правильная ли она.

def is_correct_bracket_seq(bracket_secuence: str) -> bool:
    brackets = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    stack = []
    for bracket in bracket_secuence:
        if bracket in brackets:
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False
            if bracket != brackets[stack[-1]]:
                return False
            else:
                stack.pop()
        # print(stack)
    return len(stack) == 0


print(is_correct_bracket_seq(input()))
