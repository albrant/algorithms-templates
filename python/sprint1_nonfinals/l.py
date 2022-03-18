from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    for i in range(len(shorter)):
        symbol = shorter[i]
        x = longer.find(symbol)
        if x > -1:
            longer = longer.replace(symbol, '', 1)
    return longer


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
