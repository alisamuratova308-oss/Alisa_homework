class SmartString:
    def __init__(self, string1):
        self.string1 = str(string1)
    def __len__(self):
        return len(set(self.string1))
    def __str__(self):
        return f"{self.string1}, длина {len(self.string1)},  количество уникальных символов {len(set(self.string1))}"
    def __add__(self, u_input):
        if type(u_input) == type(self.string1):
            return u_input + self.string1
        else:
            return str(u_input) + self.string1
test = SmartString("adjsd dwejf")
print(len(test))
print(str(test))
print(test + "text")
print(test + 1)