class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __len__(self):
        return round((self.x ** 2 + self.y ** 2) ** 0.5)
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    def __add__(self, new_x, new_y):
        self.x += new_x
        self.y += new_y
        return f"Vector({self.x}, {self.y})"
    def __eq__(self,new_x, new_y):
        if new_y == self.y and new_x == self.x:
            return True
        else:
            return False
