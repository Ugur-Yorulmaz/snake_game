from turtle import Turtle, Screen, turtles
import time
from snake import Snake
from food import Food
# import scoreboard
from scoreboard import Scoreboard

# form scoreboard import Scoreboard


screen=Screen()
screen.setup(width=600,height=600)
screen.title("Bu bir yilan oyunudur")
screen.bgcolor("black")
screen.tracer(0)

snake=Snake()

lokma=Food()
score=Scoreboard()

screen.listen()
screen.onkey(snake.snake_right, "Right")
screen.onkey(snake.snake_left, "Left")
screen.onkey(snake.snake_up, "Up")
screen.onkey(snake.snake_down, "Down")
game_is_on=True
while game_is_on:
    snake.move_snake()
    screen.update()
    time.sleep(0.1)

    if snake.turtles[0].distance(lokma)<40:
        lokma.locate_food()
        score.renew()
        snake.add_tail(snake.turtles[-1].position())

    if snake.turtles[0].xcor() == -300 or snake.turtles[0].xcor() == 300 or snake.turtles[0].ycor() == -300 or \
            snake.turtles[0].ycor() == 300:
        score.lose()
        game_is_on=False

    for i in range(2,len(snake.turtles)):
        if snake.turtles[0].distance(snake.turtles[i])<10:
            score.lose()
            game_is_on = False


screen.exitonclick()