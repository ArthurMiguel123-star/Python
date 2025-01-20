import turtle
import time

# Configurações da janela
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("lightblue")
wn.setup(width=800, height=600)
wn.tracer(0)

# Pontuações
score_a = 0
score_b = 0

# Raquete A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Raquete B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Bola
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2  # Aumentar a velocidade da bola
ball.dy = -0.2 # Aumentar a velocidade da bola

# Placar
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# FPS
fps_pen = turtle.Turtle()
fps_pen.speed(0)
fps_pen.color("white")
fps_pen.penup()
fps_pen.hideturtle()
fps_pen.goto(-370, 260)
fps_pen.write("FPS: 0", align="left", font=("Courier", 14, "normal"))

# Funções
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:  # Limite superior
        y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:  # Limite inferior
        y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:  # Limite superior
        y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:  # Limite inferior
        y -= 20
    paddle_b.sety(y)

# Controles do teclado
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Loop principal do jogo
last_time = time.time()
frame_count = 0

while True:
    wn.update()
    frame_count += 1
    
    current_time = time.time()
    elapsed_time = current_time - last_time

    if elapsed_time >= 1:
        fps = frame_count / elapsed_time
        fps_pen.clear()
        fps_pen.write(f"FPS: {int(fps)}", align="left", font=("Courier", 14, "normal"))
        last_time = current_time
        frame_count = 0

    # Mover a bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Verificar colisões com a borda
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        # Verificar se o Jogador A venceu
        if score_a == 10:
            pen.goto(0, 0)
            pen.write("Player A venceu!", align="center", font=("Courier", 36, "normal"))
            break

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        # Verificar se o Jogador B venceu
        if score_b == 10:
            pen.goto(0, 0)
            pen.write("Player B venceu!", align="center", font=("Courier", 36, "normal"))
            break

    # Verificar colisões com as raquetes
    if (ball.dx > 0 and 340 < ball.xcor() < 350 and
        paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1

    elif (ball.dx < 0 and -350 < ball.xcor() < -340 and
          paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
