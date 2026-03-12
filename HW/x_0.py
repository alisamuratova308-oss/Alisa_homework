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
    def break_game(self,name):
        if name == "отчистка поля":
            self.a1 = [" "," "," "]
            self.a2 = [" "," "," "]
            self.a3 = [" "," "," "]
            return "Поле отчищено"
    def vin(self):
        if self.a1 == ["X","X","X"] or self.a2 == ["X","X","X"] or self.a3 == ["X","X","X"]:
            return f"Победил игрок {self.player1}"
        elif self.a1 == ["O","O","O"] or self.a2 == ["O","O","O"] or self.a3 == ["O","O","O"]:
            return f"Победил игрок {self.player2}"
        for i in range(3):
            if self.a1[i] == self.a2[i] == self.a3[i] == "X":
                return f"Победил игрок {self.player1}"
            if self.a1[i] == self.a2[i] == self.a3[i] == "O":
                return f"Победил игрок {self.player2}"
        if (self.a1[0] == "X" and self.a2[1] == "X" and self.a3[2] == "X") or (self.a1[2] == "X" and self.a2[1] == "X" and self.a3[0] == "X"):
            return f"Победил игрок {self.player1}"
        if (self.a1[0] == "O" and self.a2[1] == "O" and self.a3[2] == "O") or (self.a1[2] == "O" and self.a2[1] == "O" and self.a3[0] == "O"):
            return f"Победил игрок {self.player2}"

test = Game('Alisa','Aleks')
while True:
    name = input('Введите имя игрока или отчистка поля: ')
    if name == "отчистка поля":
        print(test.break_game(name))
    else:
        y = int(input('Введите ряд (число от одного до трёх): '))
        x = int(input('Введите ячейку (число от одного до трёх): '))
        print(test.game_field(x,y,name))
        print(test.vin())
        
    


