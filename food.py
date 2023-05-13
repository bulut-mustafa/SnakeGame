from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self) :
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('black')
        self.speed('fastest')
        self.refresh()
        
        
    def refresh(self):
        self.goto(random.randrange(-220,220,20), random.randrange(-220,220,20))
    