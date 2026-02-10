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
    def turn(self):
        center_x = (self.x1 + self.x2)/2
        center_y = (self.y1 + self.y2)/2
        w = self.x2 - self.x1
        h = self.y2 - self.y1
        n_x1 = center_x - (h/2)
        n_y1 = center_y - (w/2)
        n_x2 = center_x + (h/2)
        n_y2 = center_y + (w/2)
        self.x1 = n_x1
        self.x2 = n_x2
        self.y1 = n_y1
        self.y2 = n_y2
    def scale(self, factor):
        center_x = (self.x1 + self.x2)/2
        center_y = (self.y1 + self.y2)/2
        w = (self.x2 - self.x1)*factor
        h =(self.y2 - self.y1)*factor
        n_x1 = center_x - (w/2)
        n_y1 = center_y - (h/2)
        n_x2 = center_x + (w/2)
        n_y2 = center_y + (h/2)
        self.x1 = n_x1
        self.x2 = n_x2
        self.y1 = n_y1
        self.y2 = n_y2
test1 = Rectangle((3,4), (3,9))
print(test1.perimeter(), test1.area())
#-----------------------------------------------

class Checkers:
    def __init__(self):
        
        pass