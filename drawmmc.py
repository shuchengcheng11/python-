import turtle

def drawmmc(x,y,t,c): #定义函数，括号内为函数的参数
    t.pensize(3)        #画笔宽度，单位像素
    t.color('white')     #设置画笔颜色为白色
    t.speed(0)          #设置画笔速度，范围0-10，1-10依次变快，0和10最快
    turtle.bgcolor('black')     #设置背景颜色
    t.penup()       #提笔，移动不绘画
    t.goto(x,y)     #设置画笔坐标，x和y分别为横坐标和纵坐标
    t.pendown()     #放下笔
    for x in range(6):  #for循环，循环6次，x取值是0-5
        t.fillcolor(c)  #填充颜色
        t.penup()       
        t.back(30)      #向后移动画笔，移动30个像素
        t.pendown() 
        t.begin_fill()  #开始填充颜色
        t.circle(20 + 5*x)  #开始画圆，半径每次增加5像素
        t.end_fill()   #结束填充
        
t = turtle.Turtle() 
drawmmc(100,100,t,'green') #调用函数
drawmmc(-130,30,t,'red')
drawmmc(-200,150,t,'yellow')
