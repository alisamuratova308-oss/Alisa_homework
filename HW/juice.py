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
    def get_concentration(self, juice_name):
        if self.total_volume == 0:
            return 0.0 
        juice_amount = self.juices.get(juice_name, 0)
        concentration = juice_amount / self.total_volume
        return concentration
t = Juice()
t = Juice()
t.add("яблочный", 200)
print(f"Концентрация яблочного сока: {t.get_concentration('яблочный')}") 
t.add("банановый", 50)  
print(f"Концентрация яблочного сока: {t.get_concentration('яблочный')}") 
t.pour_out(50, "яблочный")
print(f"Концентрация яблочного сока: {t.get_concentration('яблочный'):}") 
print(f"Концентрация бананового сока: {t.get_concentration('банановый')}")  