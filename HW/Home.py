class Potion:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def drink(self):
        return f"Вы выпили {self.name}. Cила {self.power}"
hp = Potion("зелье здоровья", 100)
print(hp.drink())
#----------------------------------------------------------
class Planet:
    def __init__(self,name,radius):
        self.name = name
        self.radius = radius
    def diametr(self):
        return self.radius * 2
#_____________________________________________________
class Meme:
    def __init__(self, template, caption):
        self.template =template
        self.caption = caption
    def post(self):
        return f"[{self.template}]: {self.caption}"
#-------------------------------------------------------------
class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def status(self):
        return f"{self.name}: {self} HP"
    def is_alive(self):
        if self.hp > 0:
            return "TRUE"
        else:
            return "FALSE"
class Wizard(Character):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self.mana = mana
    def cast_spell(self, cost):
        if self.mana >= cost:
            return f"{self.status()}, остало {self.mana - cost} маны"
        else:
            return "Нет маны"
#-----------------------------------------------------------
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def info(self):
        return f"{self.brand}, скорость {self.speed} km"
    def is_fast(self):
        if self.speed > 100:
            return "True"
        else:
            return "False"
class Car(Vehicle):
    def __init__(self, brand, speed, fuel):
        super().__init__(brand, speed)
        self.fuel = fuel
    def drive(self,km):
        if self.fuel >= km*0.1:
            return f"{self.info()}. Проехали {km}, топлива {self.fuel}"
        else:
            return "нет топлива"
#----------------------------------------------------------------------
class Coffee:
    def __init__(self, size):
        self.size = size
    def prepare(self):
        if self.size == "S":
            return f"Готовим кофе размера {self.size}"
        elif self.size == "M":
            return f"Готовим кофе размера {self.size}"
        elif self.size == "L":
            return f"Готовим кофе размера {self.size}"
        else:
            return "Такого нет"
    def prise(self):
        if self.size == "S":
            return f"100"
        elif self.size == "M":
            return f"150"
        elif self.size == "L":
            return f"200"
        else:
            return "Такого нет"

class Latte(Coffee):
    def prepare(self):
        return super().prepare()+ " с молоком"
    def prise(self):
        return super().prise() +50
#------------------------------------------------------
