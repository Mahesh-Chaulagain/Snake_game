from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# move snake
game_is_on = True
while game_is_on:
    screen.update()     # update the screen once all the segments have moved forward
    time.sleep(0.1)     # add a 1 second delay
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:  # check distance of snake head and food
        food.refresh()
        scoreboard.increase_score()

screen.exitonclick()
