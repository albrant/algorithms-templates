commands = '432111234'
number = 202

for command in commands:
    if command == '1':
        number = number << 1
        number %= 256
    elif command == '2':
        number -= 2
    elif command == '3':
        number = number >> 1
    elif command == '4':
        number -= 1
    print(command, number)
