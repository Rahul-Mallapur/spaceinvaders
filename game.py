#Space invaders using Turtle
import turtle
import os
import math
import random

#setting up the screen
window = turtle.Screen()
window.screensize(600,600)
window.title("Space Invaders")
window.bgcolor("Black")
#window.bgpic("space_background.gif")
print(window.screensize())

'''
#draw the border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("Grey")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)

border_pen.hideturtle()
'''

#create a scoring system
score = 0

score_box = turtle.Turtle()
score_box.color('white')
score_box.speed(0)
score_box.penup()
score_box.setposition(-280,280)
score_string = "Score : {}".format(score)
score_box.write(score_string, False, align = 'left', font = ('Arial', 16, 'normal'))
score_box.hideturtle()


turtle.register_shape("spaceship_r.gif")
turtle.register_shape("invader.gif")

#creating the player
player = turtle.Turtle()
player.color("Orange")
player.shape("spaceship_r.gif")
player.penup()
player.speed(0)
player.setposition(0,-260)
player.setheading(90)
playerspeed = 15

#creating the enemies
num_enemies = 5
enemies = []
enemyspeed = 2

for _ in range(num_enemies):
	enemies.append(turtle.Turtle())

for enemy in enemies:
	enemy.color('Red')
	enemy.shape('invader.gif')
	enemy.penup()
	enemy.speed(0)
	enemy.setposition(random.randint(-270,270), random.randint(100, 250))


#create the player's bullet
pbullet = turtle.Turtle()
pbullet.color('Yellow')
pbullet.shape('triangle')
pbullet.penup()
pbullet.speed(0)
pbullet.setheading(90)
pbullet.shapesize(0.4, 0.4)
pbullet.hideturtle()
pbulletspeed = 20

#ready : bullet is hidden and ready to be fired
#fire : bullet is visible on screen 
pbulletstate = 'ready'

#create right movement
def move_right():
	x = player.xcor() + playerspeed
	if x > 300:
		x = 300
	player.setx(x)

#create left movement
def move_left():
	x = player.xcor() - playerspeed
	if x < -300:
		x = -300
	player.setx(x)

#create a fire state for bullet
def fire_bullet():
	global pbulletstate

	#setting the bullet just above the player
	if pbulletstate == 'ready':
		#os.system("/Users/rahulmallapur/Documents/GitHub/spaceinvaders/shot_gun.wav&")
		os.system("afplay shot_gun.wav&")
		pbulletstate = 'fired'
		pbullet.setposition(player.xcor(), player.ycor()+5)
		pbullet.showturtle()

#check if the objects are colliding
def isCollision(Ob1, Ob2):
	#euclidean distance between the objects
	dist = math.hypot(Ob1.xcor()-Ob2.xcor(), Ob1.ycor()-Ob2.ycor())
	if dist < 15:
		return True
	else:
		return False


#listen to keyboard movement
turtle.listen()
turtle.onkey(move_right, "Right")
turtle.onkey(move_left, "Left")
turtle.onkey(fire_bullet, "space")


#create the main game environment
while True:

	for enemy in enemies:
		#move enemy continuosly
		enemy.setx(enemy.xcor() - enemyspeed)

		#reverse the enemy if it moves out of the screen
		if abs(enemy.xcor()) > 300: 
			for e in enemies:
				e.sety(e.ycor()-40)
			enemyspeed *= -1

		#check for collision between bullet and enemy
		if isCollision(pbullet, enemy):
			os.system("afplay explosion.wav&")
			pbullet.hideturtle()
			pbulletstate = 'ready'
			pbullet.setposition(0,-350) #moving the pbullet off the screen

			#uodating the score
			score += 10
			score_string = "Score : {}".format(score)
			score_box.clear()
			score_box.write(score_string, False, align = 'left', font = ('Arial', 16, 'normal'))
			
			#move the enemy and false create a new enemy
			enemy.setposition(random.randint(-290,290), random.randint(100, 250))

		#check for collision between enemy and player
		if isCollision(enemy, player):
			os.system("afplay explosion.wav&")
			player.hideturtle()
			enemy.hideturtle()
			print('Game Over')

	#move the bullet if it is fired
	if pbulletstate == 'fired':
		pbullet.sety(pbullet.ycor() + pbulletspeed)

	#if bullet is not visible on the screen, reset the state
	if pbullet.ycor() > 295: 
		pbulletstate = 'ready'
		pbullet.hideturtle()




delay = input("Press enter to finish")