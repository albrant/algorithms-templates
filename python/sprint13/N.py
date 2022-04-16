def merged_flowers(n, flower_list):
    flower_list.sort(key=lambda x: x[0])
    answer = []
    left, right = flower_list[0][0], flower_list[0][1]
    for i in range(n):
        cur_left, cur_right = flower_list[i][0], flower_list[i][1]
        if cur_left <= right:
            # сливаются промежутки
            right = max(right, cur_right)
        else:
            # начинается новый элемент, старый промежуток нужно внести
            answer.append([left, right])
            left, right = flower_list[i][0], flower_list[i][1]
    answer.append([left, right])
    return answer


def read_input():
    n = int(input())
    flower_list = []
    for _ in range(n):
        flower_list.append(list(map(int, input().split())))
    return n, flower_list


if __name__ == "__main__":
    n, flower_list = read_input()
    answer = merged_flowers(n, flower_list)
    for elem in answer:
        print(*elem, end='\n')
