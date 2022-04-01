# Тимофею нужно написать класс MyQueueSized, 
# который принимает параметр max_size, 
# означающий максимально допустимое количество элементов в очереди
class Queue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        if self.size != self.max_n:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def _size(self):
        return self.size

    def peek(self):
        if self.size == 0:
            return None
        else:
            return self.queue[self.head]


n = int(input())
queue = Queue(int(input()))

for _ in range(n):
    action = input()
    if action == 'pop':
        print(queue.pop())
    elif action == 'size':
        print(queue._size())
    elif action == 'peek':
        print(queue.peek())
    elif action.split(' ')[0] == 'push':
        x = int(action.split(' ')[1])
        queue.push(x)
