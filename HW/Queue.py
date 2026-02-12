class Queue:
    def __init__(self):
       self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items[0]
    def is_empty(self):
        if len(self.items) == 0:
            return "список пустой"
        else:
            return "список не пустой"
queue = Queue()
for item in range(10):
    queue.push(item)
    print(item)
    print(queue.items)

while not queue.is_empty():
    print(queue.items)
    print(queue.pop(),end = " ")