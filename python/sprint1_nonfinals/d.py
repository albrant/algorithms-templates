from typing import List

def get_weather_randomness(temperatures: List[int]) -> int:
    length = len(temperatures)
    if length == 1:
        return 1
    answer = 0
    temperatures.insert(0,-300)
    temperatures.append(-300)
    # print(temperatures)
    for i in range(1,length+1):
        if temperatures[i-1] < temperatures[i] > temperatures[i+1]:
            # print(temperatures[i-1], '<', temperatures[i], '>', temperatures[i+1])
            answer += 1
    return answer
        

def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures

temperatures = read_input()
print(get_weather_randomness(temperatures))
