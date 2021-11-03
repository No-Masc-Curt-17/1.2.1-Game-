import random as rand
import turtle as trtl
 
painter = trtl.Turtle()
painter.speed(0)
score_writer = trtl.Turtle()
 
 
font_setup = ("Times New Roman", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
 
#-----countdown writer-----
counter =  trtl.Turtle()
 
#-----game functions-----
def countdown():
  global timer, timer_up
  counter.clear()
  counter.penup()
  counter.goto(-350,-300)
  painter.pd()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    painter.ht()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def turtle_shape():
  painter.shapesize(rand.randint(1,5))
  colors = ["red", "gold", "black", "green", "purple", "brown", "silver"]
  colors = colors[rand.randint(0,5)]
  painter.color(colors)
  painter.shape('circle')
 
score = 0
def change_position(x,y):
  if timer_up == False:
    score_writer.clear()
    score_writer.penup()
    score_writer.goto(-200, 200)
    random_x = rand.randint(-200,200)
    random_y = rand.randint(-150,150)
    painter.penup()
    painter.goto(random_x,random_y)
    painter.pendown()
    global score
    score +=1
    painter.shapesize(rand.randint(1,5))
    colors = ["red", "gold", "black", "green", "purple", "brown", "silver"]
    colors = colors[rand.randint(0,5)]
    painter.color(colors)
    painter.shape('circle')
    colors_1 = ["cyan", "pink", "cornflower blue", "yellow", "orange", "magenta"]
    colors_1 = colors_1[rand.randint(0,4)]
    wn = trtl.Screen()
    wn.bgcolor(colors_1)
    score_writer.pendown()
    score_writer.write(score, font=font_setup)

 
 
turtle_shape()
painter.onclick(change_position)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()