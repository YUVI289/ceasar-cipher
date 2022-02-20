from turtle import *
from random import randint
import time
Up = 90
Down = 270
Right = 0
Left = 180
n = 3
xc = randint(-365,98)
yc = randint(-105,257)

list1 = []
for i in range(n):
	list1.append((xc,yc))


class Snake:
	def __init__(self):
		self.list2 = []
		self.snake_game()
		self.game_over = False

	def snake_game(self):
		n1= Turtle("turtle")
		n1.shapesize(0.7)
		n1.penup()
		n1.goto(list1[0])
		self.list2.append(n1)
		for i in range(2):
			self.add_segment(list1[i+1])
	
	def add_segment(self, i):
		snake = Turtle("square")
		snake.color("green")
		snake.shapesize(0.45)
		snake.penup()
		snake.goto(i)
		self.list2.append(snake)

	def extend(self):
		self.add_segment(self.list2[-1].pos())

	def move(self):
		for i in range(len(self.list2)-1,0,-1):
			seg = self.list2[i-1].pos()
			self.list2[i].goto(seg)
		self.list2[0].forward(11)

	def movu(self):
		if self.list2[0].heading() != Down:
			self.list2[0].setheading(Up)
	def movd(self):
		if self.list2[0].heading() != Up:
			self.list2[0].setheading(Down)
	def movr(self):
		if self.list2[0].heading() != Left:
			self.list2[0].setheading(Right)
	def movl(self):
		if self.list2[0].heading() != Right:
			self.list2[0].setheading(Left)

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.3,0.3)
        self.penup()
        self.color("red")
        self.reassign()
    
    def reassign(self):
        xc = randint(-350,90)
        yc = randint(-100,250)
        self.goto(xc,yc)
		
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(250,230)
        self.scoreupd()
        self.hideturtle()
        self.penup()
    
    def scoreupd(self):
        self.write(f"Score = {self.score}", align = "center", font = ("Arial", 25, "normal"))
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align = "center", font = ("Arial",25, "normal"))
        
    
    def incsc(self):
        self.score+=1
        self.clear()
        self.scoreupd()

score = 0

title("Snake")
screen = Screen()
bor1 = Turtle()
screen.tracer(0)	
screen.setup(900,600)
screen.bgpic("bg.png")
screen.addshape("bord.gif")
bor1.shape("bord.gif")
bor1.penup()
bor1.setposition(-140,75)
lev = screen.numinput("Level","Press easy-1, medium-2, hard-3.")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.movu, "Up")
screen.onkey(snake.movd, "Down")
screen.onkey(snake.movr, "Right")
screen.onkey(snake.movl, "Left")
	
game_over = False
while not game_over:
	screen.update()
	time.sleep(0.1/lev)
	snake.move()
	if snake.list2[0].distance(food)<9:
		food.reassign()
		snake.extend()
		scoreboard.incsc()

	if snake.list2[0].xcor() > 98 or snake.list2[0].xcor() < -380 or snake.list2[0].ycor() < -105 or snake.list2[0].ycor() > 257:
		scoreboard.game_over()
		game_over = True
		
	for i in snake.list2[1:]:
		if snake.list2[0].distance(i)<10:
			scoreboard.game_over()
			game_over = True

screen.exitonclick()