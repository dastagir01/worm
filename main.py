from turtle import Screen
from worm import Worm
import time
from food import Food
from scoreboard import Scoreboard
# from border import Border

screen = Screen()
screen.setup(1200, 1200)
# screen.bgcolor("black")
screen.bgpic('dirt.gif')
screen.update()
screen.title("Snake Game")
#screen.tracer(0) the 0 in the screen.tracer() will make the screen blank until scree.update() is called out
screen.tracer(0)

#create worm
worm = Worm()

#create food
food = Food()

#create scoreboard
Food_score = Scoreboard()
Food_score.update_scoreboard()

#include keys for screen to listen to keys
screen.listen()
screen.onkey(worm.up, "Up")
screen.onkey(worm.down, "Down")
screen.onkey(worm.left, "Left")
screen.onkey(worm.right, "Right")

# Border_for_game = Border()

playing_game = True
while playing_game:
    #first the screen.update() will display what was started for the initial starting position
    screen.update()
    time.sleep(.1)
    worm.move()
    #detect collision...
    #print(worm.head.distance(food)) to see what it is dong
    if worm.head.distance(food) < 20:
        print("nom nom nom")
        food.refresh()
        worm.extend()
        Food_score.clear()
        Food_score.increase_score()

    if worm.head.xcor() >= 600 or worm.head.xcor()  <= -600:
        # playing_game = False
        # Food_score.gameover()
        Food_score.reset()
        worm.reset()
    if worm.head.ycor() >= 600 or worm.head.ycor() <= -600:
        Food_score.reset()
        # playing_game = False
        # Food_score.gameover()
        Food_score.reset()
        worm.reset()
    for segment in worm.segments:
        #need the follow because it will compare the head with the head so we will need to pass that
        if segment == worm.head:
                pass
        elif worm.head.distance(segment) < 10:
            Food_score.reset()
            worm.reset()

            # game_is_on = False
screen.exitonclick()