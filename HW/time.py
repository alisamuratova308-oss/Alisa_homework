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
    def time(self):
        return f"{self.h}:{self.m}:{self.s}"
class Clock_r(Clock):
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
class Clock_j(Clock):
    def clock(self):
        super().clock()
        if self.h == 12 and self.m == 0 and self.s == 0:
            self.h = 6
class Clock_p(Clock):
    def clock(self):
        super().clock()
        if self.s == 7:
            s+=1
        if self.m == 7:
            m+=1
        if self.h == 7:
            h+=1


