class SmartString:
    def __init__(self, string1):
        self.string1 = string1
    def len(self):
        return len(set(self.string1))
    def str(self):
        return f"{self.string1}, длина {len(self.string1)},  количество уникальных символов {len(set(self.string1))}"
    def add(self, u_input):
        if type(u_input) == type(self.string1):
            return u_input + self.string1
        else:
            return str(u_input) + self.string1
test = SmartString("adjsd dwejf")
print(test.len())
print(test.str())
print(test.add("Hello"))
print(test.add(1))