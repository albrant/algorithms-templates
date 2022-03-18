def is_power_of_four(number: int) -> bool:
    for i in range(7):
        if 4**i == number:
            return True
    return False


print(is_power_of_four(int(input())))
