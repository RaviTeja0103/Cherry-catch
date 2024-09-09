import turtle as tu
import random
#screen
ws=tu.Screen()
tu.title("Cherry Catch")
ws.setup(width=450,height=450)
ws.bgpic("cherry2.gif")
ws.register_shape("eatcherry.gif")
ws.register_shape("eatbird.gif")

#border
ol=tu.Turtle()
ol.speed(0)
ol.penup()
ol.setposition(-200,-200)
ol.pendown()
for i in range(4):
    ol.forward(400)
    ol.left(90)
ol.hideturtle()

#Ame
ame=[]
for i in range(3):
    ame.append(tu.Turtle())
    ame[i].penup()
    ame[i].speed(0)
    ame[i].shape("eatcherry.gif")
    a=random.randint(-190,190)
    b=random.randint(-190,190)
    ame[i].right(random.randint(0,360))
    ame[i].setposition(a,b)
    
#player
t=tu.Turtle()
t.color("black")
t.shape("eatbird.gif")
t.pensize(6)
t.speed(0)
t.penup()

scr=0

def turnl():
    t.settiltangle(180)
    t.setheading(180)
def turnr():
    t.settiltangle(0)
    t.setheading(0)
def turnu():
    t.settiltangle(90)
    t.setheading(90)
def turnd():
    t.settiltangle(270)
    t.setheading(270)

tu.listen()
tu.onkey(turnl,"Left")
tu.onkey(turnr,"Right")
tu.onkey(turnu,"Up")
tu.onkey(turnd,"Down")
while True:
    t.forward(6+scr/5)
    if t.xcor()>200 or t.xcor()<-200 or t.ycor()>200 or t.ycor()<-200:
        t.penup()
        t.setposition(-150,0)
        t.hideturtle()
        t.write("GAME OVER",False,align="left",font=("Arial",40,"bold"))
        break
    for i in range(3):
        ame[i].forward(4+scr/5)
        if ame[i].xcor()>190 or ame[i].xcor()<-190 or ame[i].ycor()>190 or ame[i].ycor()<-190:
            ame[i].right(180)
        if t.xcor()<=ame[i].xcor()+10 and t.xcor()>=ame[i].xcor()-10 and t.ycor()<=ame[i].ycor()+10 and t.ycor()>=ame[i].ycor()-10:
            ame[i].setposition(random.randint(-190,190),random.randint(-190,190))
            ame[i].right(random.randint(0,360))
            scr +=1
            ol.undo()
            ol.penup()
            ol.setposition(-190,200)
            score="score:"+str(scr)
            ol.hideturtle()
            ol.write(score,False,align="left",font=("Arial",14,"normal"))
        

input()