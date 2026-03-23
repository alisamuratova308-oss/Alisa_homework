class Clock:
    def __init__(self, h=0, m=0, s=0):
        self.h = h % 24
        self.m = m % 60
        self.s = s % 60
    def clock(self):
        self.s += 1
        if self.s >= 60:
            self.s = 0
            self.m += 1
            if self.m >= 60:
                self.m = 0
                self.h += 1
                if self.h >= 24:
                    self.h = 0
    
        return f"{self.h}:{self.m}:{self.s}"
class Clock_r(Clock):
    def __init__(self, h=0, m=0, s=0):
        super().__init__(h, m, s)  
    def clock(self):
        self.s -= 1
        if self.s < 0:
            self.s = 59
            self.m -= 1
            if self.m < 0:
                self.m = 59
                self.h -= 1
                if self.h < 0:
                    self.h = 23
        return f"{self.h}:{self.m}:{self.s}"
class Clock_j(Clock):
    def __init__(self, h=0, m=0, s=0):
        super().__init__(h, m, s)
    def clock(self):
        super().clock()
        if self.h == 12 and self.m == 0 and self.s == 0:
            self.h = 6
        return f"{self.h}:{self.m}:{self.s}"
class Clock_p(Clock):
    def __init__(self, h=0, m=0, s=0):
        super().__init__(h, m, s)
    def clock(self):
        super().clock()
        if self.s == 7 or self.s == 3:
            self.s+=1
        if self.m == 7 or self.m == 3:
            self.m+=1
        if self.h == 7 or self.h == 3:
            self.h+=1
        return f"{self.h}:{self.m}:{self.s}"
test = Clock(3,40,3)
print(test.clock())
test2 = Clock_r(2,4,6)
print(test2.clock())
test3 = Clock_j(11,59,59)
print(test3.clock())
test4 = Clock_p(2,6,2)
print(test4.clock())


