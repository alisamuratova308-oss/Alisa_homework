class MyDeque:
    def __init__(self):
        self.spisok = []
    def __len__(self):
        return len(self.spisok)

    def __repr__(self):
        return f"Deque({self.spisok})"
    def append(self,x):
        self.spisok.append(x)
    def pop(self):
        return self.spisok.pop()
    def popleft(self):
        return self.spisok.pop(0)
deque = MyDeque()
deque.append(1)
deque.append(2)
print(deque)          
print(deque.pop())   
print(deque.popleft()) 
print(len(deque))     
print(deque)         
        
    