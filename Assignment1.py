import turtle

# 设置画布
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Pretty Flower")

# 创建画笔
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

# 画花瓣的函数
def draw_petal():
    t.fillcolor("#FF69B4")  # 粉红色
    t.begin_fill()
    for _ in range(2):
        t.circle(100, 60)
        t.left(120)
    t.end_fill()

# 画花茎
t.penup()
t.goto(0, -200)  # 从更低的位置开始画茎
t.setheading(90)  # 朝上
t.pendown()
t.color("green")
t.pensize(4)
t.forward(100)  # 画茎的下部分



# 画茎的上部分
t.setheading(90)  # 重新朝上
t.forward(50)

# 回到花茎顶端画花瓣
t.penup()
t.goto(0, -50)
t.setheading(0)  # 重置方向
t.pendown()
t.color("black")
t.pensize(2)

# 画五片花瓣
for _ in range(5):
    draw_petal()
    t.left(72)

# 画花心
t.penup()
t.goto(0, -60)  # 调整花心位置，使其居中
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(10)
t.end_fill()

# 隐藏画笔
t.hideturtle()

# 保持窗口打开
screen.mainloop()
