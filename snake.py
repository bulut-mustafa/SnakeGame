from turtle import Turtle
class Snake:
    def __init__(self) -> None:
        self.snakes = []
        for i in range(0,3):
            snake = Turtle(shape='square')
            snake.penup()
            snake.setposition(i*(-20), 0)
            self.snakes.append(snake)


    def go_up(self):
        if self.snakes[0].heading() != 270:
                self.snakes[0].setheading(90)
    def go_down(self):
        if self.snakes[0].heading() != 90:
                self.snakes[0].setheading(270)
    def go_right(self):
        if self.snakes[0].heading() != 180:
                self.snakes[0].setheading(0)
    def go_left(self):
        if self.snakes[0].heading() != 0:
                self.snakes[0].setheading(180)
                
    def move(self):
        
        for i in range(len(self.snakes)-1, 0, -1):
            self.snakes[i].goto(self.snakes[i-1].xcor(),self.snakes[i-1].ycor())
        self.snakes[0].forward(20)
        
    def eat(self):
        snake = Turtle(shape='square')
        snake.penup()
        snake.setposition(self.snakes[-1].position())
        self.snakes.append(snake)
    
    
    def crash(self):
        if  self.snakes[0].xcor() > 230:
            return True
        if  self.snakes[0].xcor() < -230:
            return True
        if  self.snakes[0].ycor() > 230:
            return True
        if  self.snakes[0].ycor() < -230:
            return True
        for i in range(len(self.snakes)-1,0,-1):
            if self.snakes[0].distance(self.snakes[i]) < 10:
                return True
        
            
       