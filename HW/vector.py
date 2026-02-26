class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def len(self):
        return round((self.x ** 2 + self.y ** 2) ** 0.5)
    def str(self):
        return f"Vector({self.x}, {self.y})"