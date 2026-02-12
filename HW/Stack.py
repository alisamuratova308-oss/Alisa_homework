class Stack:
    def __init__(self):
        self.items =[]
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items[0]
    def is_empty(self):
        if len(self.items) == 0:
            return "список пустой"
        else:
            return "список не пустой"