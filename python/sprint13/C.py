def substr(sub, string):
    start = 0
    end = len(string) - len(sub) + 2
    for letter in sub:
        find_index = string.find(letter, start)
        if find_index == -1:
            return False
        start = find_index + 1
    return True


if __name__ == '__main__':
    s_string = input()
    t_string = input()
    if len(s_string) > len(t_string):
        print(False)
    else:
        print(substr(s_string, t_string))
