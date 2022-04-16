# id-67438270
def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if (
            (array[i][1] > array[begin][1]) or
            (
                (array[i][1] == array[begin][1]) and
                (array[i][2] < array[begin][2])
            ) or
            (
                (array[i][1] == array[begin][1]) and
                (array[i][2] == array[begin][2]) and
                (array[i][0] <= array[begin][0])
            )
        ):
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quick_sort_in_place(array, begin, end):
    if begin >= end:
        return
    pivot = partition(array, begin, end)
    quick_sort_in_place(array, begin, pivot-1)
    quick_sort_in_place(array, pivot+1, end)


def read_input():
    n = int(input())
    participants = []
    for _ in range(n):
        name, solved_tasks, fine = input().split()
        participants.append([name, int(solved_tasks), int(fine)])
    return n, participants


if __name__ == '__main__':
    participants_count, participants = read_input()
    quick_sort_in_place(participants, 0, participants_count-1)
    print(*[user[0] for user in participants], sep='\n')
