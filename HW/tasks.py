class Koplika:
    def __init__(self):
        self.balanse = 100
        self.t = None
    def polozhit(self, amount):
        self.balanse += amount
        return f"Вы пополнили баланс на {amount} рублей"
    def snyat(self, amount):
        self.balanse -= amount
        return f"Вы сняли {amount}"

    def postavit_tzel(self, t_amount):
        self.t = t_amount
        return f"Цель накоплений {self.t}"
    def hvatit_na_tzel(self):
        if self.balanse >= self.t:
            return "Вы накопили на цель"
        else:
            return "Недостаточно средств для достижения цели."
koplika = Koplika()
while True:
    u_input = input("Ввидите polozhit, snyat, postavit_tzel, hvatit_na_tzel или выход: ")
    if u_input == "выход":
        break
    elif u_input == "polozhit":
        amount = int(input("Введите суммму: "))
        print(koplika.polozhit(amount))
    elif u_input == "snyat":
        amount = int(input("Введите суммму: "))
        print(koplika.snyat(amount))
    elif u_input == "postavit_tzel":
        t_amount = input("Введите цель: ")
        print(koplika.postavit_tzel(t_amount))
    else:
        print(koplika.hvatit_na_tzel())



    