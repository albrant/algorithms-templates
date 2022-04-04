from collections import deque

queue = deque([])
size = 0

n = int(input())
for _ in range(n):
    action = input()
    if action.split()[0] == 'put':
        queue.append(int(action.split()[1]))
        size += 1
    elif action == 'size':
        print(size)
    elif action == 'get':
        if size == 0:
            print('error')
        else:
            print(queue.popleft())
            size -= 1
