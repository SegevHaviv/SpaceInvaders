import turtle
import os
import math
import random


# Window object
wn = turtle.Screen()
wn.setup(800, 750, None, None)
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("giph2.gif")

# Register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")


# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()


# Creating a player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

# Set the initial score
score = 0

# Drawing the score
score_pen = turtle.Turtle();
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
scoreString = "Score: %s" % score
score_pen.write(scoreString,False,align="left",font=("Arial",14,"normal"))
score_pen.hideturtle()

playerSpeed = 15
enemySpeed = 10
enemyInitialX = 100
enemyInitialY = 90
index = 0

# Set number of enemies
num_of_enemies = 10

# Empty list of enemies
enemies = []

# Add enemies to the list
for i in range(num_of_enemies):
    enemies.append(turtle.Turtle())


for enemy in enemies:
    index += 1
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    enemy.setposition(enemyInitialX, enemyInitialY)
    if index == num_of_enemies / 2:
        enemyInitialX += 10

    enemyInitialY += 15

# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletSpeed = 85

# Bullet state
# ready - ready to fie
# fire - bullet is firing
bulletState = "ready"


# Moving the player right&left
def move_left():
    x = player.xcor()  # start of game it'd be zero
    x -= playerSpeed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()  # start of game it'd be zero
    x += playerSpeed
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    # Declare bulletState as a global if it needs changed
    global bulletState

    if bulletState == "ready":
        bulletState = "fire"
        # Move the bullet to above the player
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x,y+10)
        bullet.showturtle()


# Checking if a fire hit the target
def is_collision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


# Keyboard binding
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Main game loop
while True:

    for enemy in enemies:
        # Move Enemy
        enemy.setx(enemy.xcor() + enemySpeed)

        # Move enemy back and down
        if enemy.xcor() > 280 or enemy.xcor() < -280:
            enemySpeed *= -1
            for e in enemies:
                e.sety(e.ycor() - 40)

        # Check for collision between bullet and enemy
        if is_collision(bullet, enemy):
            # Reset the bullet
            bullet.hideturtle()
            bullet.setposition(0, -400)
            enemy.setposition(random.randint(-200, 200), random.randint(100, 250))
            # Raising the score
            score += 10
            score_pen.clear()
            scoreString = "Score : %s" % score
            score_pen.write(scoreString, False, align="left", font=("Arial", 14, "normal"))
            bullet.hideturtle()
            bulletState = "ready"

        if is_collision(enemy, player):
            player.hideturtle()
            enemy.hideturtle()
            print("Game over")
            break

    # Move the bullet
    if bulletState == "fire":
        y = bullet.ycor()
        y += bulletSpeed
        bullet.sety(y)

    # Checking if bullet reached to top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletState = "ready"





