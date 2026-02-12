class Rectangle:
    def __init__(self,cort1,cort2):
        self.x1,self.y1 = cort1
        self.x2,self.y2 = cort2
    def perimeter(self):
        return f"Пириметр - {(self.x2 - self.x1 + self.y2 - self.y1)*2}"
    def area(self):
        return f"Площать - {(self.x2 - self.x1) * (self.y2 - self.y1)}"
    def get_pos(self):
        return f"{self.x1}.{self.y1}"
    def get_size(self):
        return f"ширина - {self.x2 - self.x1}, высота - {self.y2 - self.y1}"
    def move(self, dx, dy):
        self.x1 += dx
        self.x2 += dx
        self.y1 += dy
        self.y2 += dy
    def resize(self, width, height):
        self.x2 = self.x1 + width
        self.y2 = self.y1 + height


test1 = Rectangle((3,4), (5,10))
print(test1.perimeter(), test1.area())
print(test1.get_size())
print((test1.x2 - test1.x1 + test1.y2-test1.y1)*2 - (test1.x2 - test1.x1)- (test1.y2 - test1.y1) )