class Stack:
    def __init__(self):
        self.items = []
        self.maximum = -10**100
        self.length = 0

    def push(self, item):
        self.maximum = max(self.maximum, item)
        self.items.append(self.maximum)
        self.length += 1

    def pop(self):
        if self.length == 0:
            print('error')
        else:
            if self.length > 1:
                self.maximum = self.items[-2]
            else:
                self.maximum = -10**100
            self.length -= 1
            return self.items.pop()

    def get_max(self):
        if self.maximum == -10**100:
            return None
        return self.maximum


stack = Stack()
n = int(input())
for _ in range(n):
    action = input()
    if action == 'pop':
        stack.pop()
    elif action == 'get_max':
        print(stack.get_max())
    elif action.split(' ')[0] == 'push':
        x = int(action.split(' ')[1])
        stack.push(x)
    # print(stack.items)
