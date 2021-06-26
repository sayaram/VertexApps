class Stack:
    def __init__(self):
        self.Stack = []

    def push(self, data):
        self.Stack.append(data)

    def size(self):
        return len(self.Stack)

    def isEmpty(self):
        if len(self.Stack)<=0:
            return True

    def pop(self):
        if len(self.Stack) > 0:
            return self.Stack.pop()

def reverse(txt: str) -> str:
    sk = Stack()
    for c in txt:
        sk.push(c)
    string = ""
    for i in range(sk.size()):
        string += sk.pop()
    return string

print(reverse("Sayaram Gattu"))