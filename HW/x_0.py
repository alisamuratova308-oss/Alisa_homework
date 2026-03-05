class Plaers:
    
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

class Game(Plaers):
    
    def __init__(self, player1, player2):
        super().__init__(player1, player2)
        self.a1 = [" "," "," "]
        self.a2 = [" "," "," "]
        self.a3 = [" "," "," "]
    
    def game_field(self,x,y,name):
        b = '-------'
        b1 = '-------'
        b2 = '-------'
        b3 = '-------'
        if 0 < x <= 3 and 0 < y <= 3:
            if name == self.player1:
                if y == 1:
                    self.a1[x-1] = "X"
                elif y == 2:
                    self.a2[x-1] = "X"
                elif y == 3:
                    self.a3[x-1] = "X"
            elif name == self.player2:
                if y == 1:
                    self.a1[x-1] = "O"
                elif y == 2:
                    self.a2[x-1] = "O"
                elif y == 3:
                    self.a3[x-1] = "O"
            else:
                print("Такого имени нет")
        return f'''{b}
{"|" + "|".join(self.a1) + "|"}
{b1}
{"|" +"|".join(self.a2) + "|"}
{b2}
{"|"+ "|".join(self.a3)  +"|"}
{b3}
'''


test = Game('Alisa','Aleks')
# print(test.game_field(1,1,'Alisa'))  
while True:
    # u_input = input("Введите играть или выход")
    # if u_input == "выход":
    #     break
    # elif u_input == "играть":
    name = input('Введите имя игрока: ')
    y = int(input('Введите ряд (число от одного до трёх): '))
    x = int(input('Введите ячейку (число от одного до трёх): '))
    print(test.game_field(x,y,name))

