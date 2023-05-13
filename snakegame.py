from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score
# setting the screen
screen = Screen()
screen.setup(480,480)
screen.title('Snake Game')
screen.listen()

screen.tracer(0)
# setting the snake

snake = Snake()
food = Food()
score = Score()
screen.onkey(snake.go_up, 'Up')
screen.onkey(snake.go_down, 'Down')
screen.onkey(snake.go_right, 'Right')       
screen.onkey(snake.go_left, 'Left')


is_game_on = True

def collision(food, snake):
    for segment in snake.snakes[1:]:
        if food.distance(segment) < 5:
            return True
while is_game_on:
    screen.update()
    time.sleep(0.07)
    
    
    snake.move()
    while collision(food, snake):
        food.refresh()
    
    if snake.snakes[0].distance(food) < 5:
        snake.eat()
        food.refresh()
    
    if snake.crash():
        score.game_over()
        is_game_on = False    

screen.exitonclick()