class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __len__(self):
        return round((self.x ** 2 + self.y ** 2) ** 0.5)
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    def __add__(self, new_vector):
        if type(new_vector) != type(self):
            raise TypeError("Это не вектор")
        self.x += new_vector.x
        self.y += new_vector.y
        return f"Vector({self.x }, {self.y})"
    def __eq__(self,new_vector):
        if type(new_vector) != type(self):
            raise TypeError("Это не вектор")
        if new_vector.y == self.y and new_vector.x == self.x:
            return True
        else:
            return False
test = Vector2D(6,9)
test2 = Vector2D(8,4)
test3 = Vector2D(6,9)
print(test.__len__())
print(test.__str__())
# print(test + test2)
# print(test + test3)
# print(test + 4)
print(test == test2)
print(test == test3)
print(test == 0)