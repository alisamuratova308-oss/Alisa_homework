# Реализовать класс Game и Player
# В цикле while true ожидать сначала номер игрока, потом действие игрока: move_up, move_down, move_left, move_right.
# При получении команды меняем координаты x и y игрока соответственно при помощи одного из 4 методов.
# Game хранит словарь айди-игрок и вызывает действие у каждого из них при получении номера игрока.

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    def player_get_id(self, id):
        if id ==1:
            return self.player1
        elif id ==2:
            return self.player2
        else:
            return "ошибка"
class Player:
        def __init__(self, speed=1):
            self.x = 0
            self.y = 0
            
            self.speed = speed
        def move_up(self):
            self.y += 1*self.speed
        def move_down(self):
            self.y -=1*self.speed
        def move_left(self):
            self.x -=1*self.speed
        def move_right(self):
            self.x += 1*self.speed

#=======================================================

    



    


            
        
             
             
             




       