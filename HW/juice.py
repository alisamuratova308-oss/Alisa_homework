class Juice:
    def __init__(self):
        self.juices = {} 
        self.total_volume = 0 

    def add(self, name, amount):
        if name in self.juices:
            self.juices[name] += amount 
        else:
            self.juices[name] = amount 
        self.total_volume += amount  
    def pour_out(self, amount, j_name):
        if j_name in self.juices:
            self.juices[j_name] -= amount
            self.total_volume -= amount
    def get_concentration_f(self):
        if self.total_volume == 0:
            return 0
        juice_f = next(iter(self.juices))
        juice_amount = self.juices[juice_f]
        concentration = juice_amount / self.total_volume
        return concentration
t = Juice()
t.add("яблочный", 200)
print(f"Концентрация первого сока: {t.get_concentration_f()}") 
t.add("банановый", 50)  
print(f"Концентрация первого сока: {t.get_concentration_f()}") 
t.pour_out(50, "яблочный")
print(f"Концентрация первого сока: {t.get_concentration_f()}") 


