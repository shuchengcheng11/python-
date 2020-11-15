import turtle

def drawmmc(x,y,t,c):
    t.pensize(3)
    t.color('white')
    t.speed(0)
    turtle.bgcolor('black')
    t.penup()
    t.goto(x,y)
    t.pendown()
    for x in range(6):
        t.fillcolor(c)
        t.penup()
        t.back(30)
        t.pendown()
        t.begin_fill()
        t.circle(20 + 5*x)
        t.end_fill()
        
t = turtle.Turtle()
drawmmc(100,100,t,'green')
drawmmc(-130,30,t,'red')
drawmmc(-200,150,t,'yellow')