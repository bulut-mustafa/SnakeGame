from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
    
    def game_over(self):
        self.write('Game over', align='center',font=('Arial', 30, 'normal'))
        