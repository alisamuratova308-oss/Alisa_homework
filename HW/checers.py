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