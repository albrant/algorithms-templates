def is_palindrome(line: str) -> bool:
    line = line.lower()
    line = "".join([i for i in line if not(i in (',.: '))])
    return line == line[::-1]


print(is_palindrome(input().strip()))
