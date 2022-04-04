# id = 66757931

class DequeIsEmptyPopError(Exception):
    pass


class DequeIsFullPushError(Exception):
    pass


class Deque:
    def __init__(self, capacity):
        self._items = [None] * capacity
        self._capacity = capacity
        self._head = 0
        self._tail = -1
        self._size = 0

    def print(self):
        print([self._size, self._head, self._tail], end=': ')
        for i in range(self._head, self._tail + 1):
            print(self._items[i], end='->')
        print()

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._capacity

    def push_back(self, item):
        if not self.is_full():
            self._tail = (self._tail + 1) % self._capacity
            self._items[self._tail] = item
            self._size += 1
        else:
            raise DequeIsFullPushError

    def push_front(self, item):
        if not self.is_full():
            self._head -= 1
            self._items[self._head] = item
            self._size += 1
        else:
            raise DequeIsFullPushError

    def pop_front(self):
        if self.is_empty():
            raise DequeIsEmptyPopError
        x = self._items[self._head]
        self._items[self._head] = None
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        return x

    def pop_back(self):
        if self.is_empty():
            raise DequeIsEmptyPopError
        x = self._items[self._tail]
        self._items[self._tail] = None
        self._tail -= 1
        self._size -= 1
        return x


if __name__ == '__main__':
    count_actions = int(input())
    my_deque = Deque(int(input()))

    for _ in range(count_actions):
        action_split = input().split()
        action = action_split[0]
        if len(action_split) == 1:
            try:
                print(getattr(my_deque, action)())
            except DequeIsEmptyPopError:
                print('error')
        elif len(action_split) == 2:
            item_for_push = int(action_split[1])
            try:
                getattr(my_deque, action)(item_for_push)
            except DequeIsFullPushError:
                print('error')
