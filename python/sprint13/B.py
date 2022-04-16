NUM_CIF = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def numero(string_number, k=0, answer=''):
    if k >= len(string_number):
        print(answer, end=' ')
    else:
        letters = NUM_CIF[string_number[k]]
        for letter in letters:
            answer = answer[:k] + letter + answer[k+1:]
            numero(string_number, k + 1, answer)


numero(input())
