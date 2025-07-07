from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen ()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
# https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.tracer
screen.tracer(0) # Turn turtle animation on(=1)/off(=0) --disable auto screen refresh

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

paused = False
def toggle_pause():
    global paused
    paused = not paused

screen.onkey(toggle_pause, "space") # Every time you hit space, it flips the paused flag.

game_is_on = True
while game_is_on:
    screen.update()  # To be used when tracer is turned off -- manually update
    time.sleep(0.2)  # sleep 0.1 sec = add 0.1 sec delay after each segment moves
    if not paused:
        snake.move()

        #Detect collision with food
        if snake.head.distance(food) < 15: #remember our food(turtle) has size circle 10*10
            food.refresh()
            scoreboard.clear() # clear old score before show new score after snake eats food
            scoreboard.increase_score()
            snake.add_seg()

        #Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.reset_score()
            snake.restart_snake()

        #Detect collision with its own tail
        for segment in snake.segments[1:]:  # <- using slicing method by skipping the head itself :
                                            # [1:] means get all elements of the list snake.segments,
                                            # starting from index 1 up to the end.
                                            # (alternative you can write) if segment = snake.segments: pass
            if snake.head.distance(segment) < 10:
                scoreboard.reset_score()
                snake.restart_snake()

            # if snake.head.position() in snake.position_body():
            #     game_is_on = False
            # This method won't work because .position() method returns a tuple of floats
            # So even though visually the head overlaps the tail, the float tuples aren’t exactly equal
            # head.position() may be like (20.0000000001, 0.0)
            # BUT the body’s position list contains: [(20.0, 0.0), (0.0, 0.0), (-20.0, 0.0)]
            # Instead of testing exact position equality, test if the distance
            # between the head and any body segment is less than a threshold (e.g., 10 pixels)

screen.exitonclick()