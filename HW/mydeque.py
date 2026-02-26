class MyDeque:
    def __init__(self):
        self.spisok = []
    def __len__(self):
        return len(self.spisok)

    def __repr__(self):
        return f"Deque({self.spisok})"
    def append(self,x):
        self.spisok.append(x)
    def appendleft(self, x):
        self.spisok.reverse()
        print(self.spisok)
        self.spisok.append(x)
        print(self.spisok)
        self.spisok.reverse()
        print(self.spisok)
        pass
    def pop(self):
        return self.spisok.pop()
    def popleft(self):
        return self.spisok.pop(0)
deque = MyDeque()
deque.append(1)
deque.append(2)
deque.appendleft(5)
print(deque)          
print(deque.pop())   
print(deque.popleft()) 
print(len(deque))     
print(deque)         
        
    