# class Rectangle:
#     def __init__(self,cort1,cort2):
#         self.x1,self.y1 = cort1
#         self.x2,self.y2 = cort2
#     def perimeter(self):
#         return f"Пириметр - {(self.x2 - self.x1 + self.y2 - self.y1)*2}"
#     def area(self):
#         return f"Площать - {(self.x2 - self.x1) * (self.y2 - self.y1)}"
#     def get_pos(self):
#         return f"{self.x1}.{self.y1}"
#     def get_size(self):
#         return f"ширина - {self.x2 - self.x1}, высота - {self.y2 - self.y1}"
#     def move(self, dx, dy):
#         self.x1 += dx
#         self.x2 += dx
#         self.y1 += dy
#         self.y2 += dy
#     def resize(self, width, height):
#         self.x2 = self.x1 + width
#         self.y2 = self.y1 + height
#     def turn(self):
#         center_x = (self.x1 + self.x2)/2
#         center_y = (self.y1 + self.y2)/2
#         w = self.x2 - self.x1
#         h = self.y2 - self.y1
#         n_x1 = center_x - (h/2)
#         n_y1 = center_y - (w/2)
#         n_x2 = center_x + (h/2)
#         n_y2 = center_y + (w/2)
#         self.x1 = n_x1
#         self.x2 = n_x2
#         self.y1 = n_y1
#         self.y2 = n_y2
#     def scale(self, factor):
#         center_x = (self.x1 + self.x2)/2
#         center_y = (self.y1 + self.y2)/2
#         w = (self.x2 - self.x1)*factor
#         h =(self.y2 - self.y1)*factor
#         n_x1 = center_x - (w/2)
#         n_y1 = center_y - (h/2)
#         n_x2 = center_x + (w/2)
#         n_y2 = center_y + (h/2)
#         self.x1 = n_x1
#         self.x2 = n_x2
#         self.y1 = n_y1
#         self.y2 = n_y2
# test1 = Rectangle((3,4), (3,9))
# print(test1.perimeter(), test1.area())
# #-----------------------------------------------

# class Checkers:
#     def __init__(self):
#         self.a = ["X", "B", "X", "B","X", "B", "X", "B" ]
#         self.b = ["B", "X", "B", "X","B", "X", "B", "X" ]
#         self.c = ["X", "B", "X", "B","X", "B", "X", "B" ]
#         self.d = ["B", "X", "B", "X","B", "X", "B", "X" ]
#         self.e = ["X", "B", "X", "B","X", "B", "X", "B" ]
#         self.f = ["B", "X", "B", "X","B", "X", "B", "X" ]
#         self.g = ["X", "B", "X", "B","X", "B", "X", "B" ]
#         self.h = ["B", "X", "B", "X","B", "X", "B", "X" ]
#         self.spisok = ["a", "b", "c", "d", "e", "f", "g", "h"]
#     def move(self, f, t):
#         st = 0
#         if f + t > 8:
#             while True:
#                 if f + t > 8:
#                     break
#                 else:
#                     t = t -8
#                     st+=1
#         if st == 0:
#             self.a[f + t] = "Ш"
#         else:
#             pass

#=======================================================

# class Queue:
#     def __init__(self):
#        self.items = []
#     def push(self, item):
#         self.items.append(item)
#     def pop(self):
#         return self.items[0]
#     def is_empty(self):
#         if len(self.items) == 0:
#             return "список пустой"
#         else:
#             return "список не пустой"
# queue = Queue()
# for item in range(10):
#     queue.push(item)
# while not queue.is_empty():
#     print(queue.pop(),end = " ")
#=======================================================

# class Stack:
#     def __init__(self):
#         self.items =[]
#     def push(self, item):
#         self.items.append(item)
#     def pop(self):
#         return self.items[0]
#     def is_empty(self):
#         if len(self.items) == 0:
#             return "список пустой"
#         else:
#             return "список не пустой"


