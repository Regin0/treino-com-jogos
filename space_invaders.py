import turtle
import os
import math
import random

wn = turtle.Screen()
wn.title('Space Invaders')
wn.bgcolor('black')


#Desenhando a borda
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('red')
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range (4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()


#Set the score to 0
score = 0

#Desenhando o score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial",14, "normal"))
score_pen.hideturtle()

#Player turtle
player = turtle.Turtle()
player.color('blue')
player.shape('triangle')
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15

#Escolhendo o numero de inimigo
number_of_enemies = 5
#Criando uma lista vazia de inimigos
enemies = []

#Adicionando inimigos na lista
for i in range(number_of_enemies):
    #Criando o inimigo
   enemies.append(turtle.Turtle()) 

for enemy in enemies:
    enemy.color('purple')
    enemy.shape('circle')
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x,y)
    # enemy.setposition(-200,-200)

enemyspeed = 2

#Munição do player

bullet = turtle.Turtle()
bullet.color('white')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

#Estado da bala
#ready - ready to fire
#fire - bullet is firing
bulletstate = 'ready'

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #Declare bulletsate as a global if it needs changed
    global bulletstate
    if bulletstate == 'ready':
        bulletstate = 'fire'
        #Movendo a bala pra cima do player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False
#Create keyboard bindings
wn.listen()
wn.onkeypress(move_left, 'a')
wn.onkeypress(move_right, 'd')
wn.onkeypress(fire_bullet, 'space')


#Main game loop 
while True:

    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        if enemy.xcor() > 280:
            #Move todos os inimigos para baixo
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Muda a direção do inimigo
            enemyspeed *= -1

        if enemy.xcor() < -280:
            #Move todos os inimigos para baixo
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Muda a direção do inimigo
            enemyspeed *= -1

            #Checando por uma colisão entre a bala e o enimigo
        if isCollision(bullet, enemy):
            #Reset the bullet
            bullet.hideturtle()
            bulletstate = 'ready'
            bullet.setposition(0, -400)
            enemy.setposition(-200,250)
            #Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x,y)
            #Update the score
            score += 10
            scorestring = f"Score: {score}"
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial",14, "normal"))

        if isCollision(enemy, player):
            player.hideturtle()
            enemy.hideturtle()
            print('Game Over malando')
            break

    #Movendo a bala
    if bulletstate == 'fire':
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #Checando se a bala passou da borda de cima
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = 'ready'

