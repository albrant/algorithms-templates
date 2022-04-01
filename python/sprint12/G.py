class Stack:
    def __init__(self):
        self.items = []
        self.maximum = -10**100

    def push(self, item):
        self.maximum = max(self.maximum, item)
        self.items.append(item)

    def pop(self):
        last_elem = self.items.pop()
        if last_elem == self.maximum:
            if self.length == 0:
                self.maximum = -10**100
            else:
                self.maximum = max(self.items)
        return last_elem

    def length(self):
        return len(self.items)

    def get_max(self):
        if len(self.items) == 0 or self.maximum == -10**100:
            return None
        return self.maximum

stack = Stack()
n = int(input())
for _ in range(n):
    action = input()
    if action == 'pop':
        try:
            stack.pop()
        except:
            print('error')
    elif action == 'get_max':
        print(stack.get_max())
    elif action.split(' ')[0] == 'push':
        x = int(action.split(' ')[1])
        stack.push(x)
    print(stack.items)
