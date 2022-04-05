# id = 66774193

class DequeIsEmptyPopError(Exception):
    pass


class DequeIsFullPushError(Exception):
    pass


class Deque:
    def __init__(self, capacity):
        self.__items = [None] * capacity
        self.__capacity = capacity
        self.__head = 0
        self.__tail = -1
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def is_full(self):
        return self.__size == self.__capacity

    def push_back(self, item):
        if not self.is_full():
            self.__tail = (self.__tail + 1) % self.__capacity
            self.__items[self.__tail] = item
            self.__size += 1
        else:
            raise DequeIsFullPushError

    def push_front(self, item):
        if not self.is_full():
            self.__head -= 1
            self.__items[self.__head] = item
            self.__size += 1
        else:
            raise DequeIsFullPushError

    def pop_front(self):
        if self.is_empty():
            raise DequeIsEmptyPopError
        head_item = self.__items[self.__head]
        self.__items[self.__head] = None
        self.__head = (self.__head + 1) % self.__capacity
        self.__size -= 1
        return head_item

    def pop_back(self):
        if self.is_empty():
            raise DequeIsEmptyPopError
        tail_item = self.__items[self.__tail]
        self.__items[self.__tail] = None
        self.__tail -= 1
        self.__size -= 1
        return tail_item


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
