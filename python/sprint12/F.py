class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def get_max(self):
        if len(self.items) == 0:
            return None
        return max(self.items)


stack = Stack()
n = int(input())
for _ in range(n):
    action = input()
    if action == 'pop':
        try:
            stack.pop()
        except Exception:
            print('error')
    elif action == 'get_max':
        print(stack.get_max())
    elif action.split(' ')[0] == 'push':
        x = int(action.split(' ')[1])
        stack.push(x)
