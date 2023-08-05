import turtle  #import turtle to the code
import random  #import random to the code
import time    #import time to the code

snake_game = turtle.Screen()
#define the display for the game
def display():
    snake_game.title("Marcellus' Snake Game")
    snake_game.bgcolor('Green')
    snake_game.setup(width = 660, height = 740)

line = turtle.Turtle()
#define the title for the game
def title():
    line.hideturtle()
    line.penup()
    line.goto(0, 250)
    line.write("Contact: 0\t Time: 0 \t Motion: Paused", align="center", font=("Arial", 14, "normal"))

game_border = turtle.Turtle()
#define the line border for the game table
def border():
    game_border.penup()
    game_border.hideturtle()
    game_border.setposition(-250,-290)
    game_border.speed(0)
    game_border.pendown()
    game_border.pensize(1)
    game_border.color("black")
    game_border.fd(500)
    game_border.lt(90)
    game_border.fd(580)
    game_border.lt(90)
    game_border.fd(500)
    game_border.lt(90)
    game_border.fd(580)
    game_border.lt(90)
    game_border.penup()
    game_border.setposition(-250, 230)
    game_border.hideturtle()
    game_border.speed(0)
    game_border.pendown()
    game_border.forward(500)

#define the click for start the game
def click_start(x, y):
    global introduction, food, foodx, foody, number_food
    introduction.clear()
    generate_food()
    snake_game.onclick(None)
    snake_game.ontimer(head_move, 100)
    snake_game.ontimer(monster_move, 400)
    while True:
        snake_game.update()

#define the introduction page
def first_page():
    global introduction
    introduction = turtle.Turtle()
    introduction.hideturtle()
    introduction.penup()
    introduction.goto(-230, 70)
    introduction.write("Welcome to Marcellus' snake game! \n" + \
                "Use four arrow keys to move your snake. \n" + \
                "You can pause the snake with space button. \n" + \
                "Don't let the monster catch you and eat all of the food! \n" + \
                "Click screen to continue.", font=("Arial", 12, "normal"))

head = turtle.Turtle()
#define the turtle for the head
def head_spec():
    head.speed(0)
    head.shape("square")
    head.color("Orange")
    head.penup()
    x = random.randint(40, 240)
    head.goto(x, 0)
    head.speed(1)

monster = turtle.Turtle()
#define the turtle for the monster
def monster_spec():
    monster.speed(0)
    monster.shape("square")
    monster.color("Purple")
    monster.penup()
    x = random.randint(-240, -40)
    y = random.randint(-270, 200)
    monster.goto(x, y)
    monster.speed(1)

snake = True
bodys = []  #list for the snake body
length = 5  #the initial number of snake body
head.direction = "move"
motion = ''
#define the movement for the snake
def head_move():
    global length, number_food, snake, motion, bodys
    snake_game.tracer(0)
    bodys.append((head.xcor(), head.ycor()))
    #stamp new body for the snake
    if len(head.stampItems) < length:
        head.color('black')
        head.stamp()
        head.color("Orange")
    else:
        head.color('black')
        head.stamp()
        head.color("Orange")
        head.clearstamps(1)
        bodys.pop(1)
    snake_game.tracer(1)
    #define the snake movement for up
    if head.direction == "up":
        y = head.ycor()
        motion = 'up'
        if y + 20 <= 220:
            head.sety(y+20) 
    #define the snake movement for down
    if head.direction == "down":
        y = head.ycor()
        motion = 'down'
        if y - 20 >= -290:
            head.sety(y-20)
    #define the snake movement for right
    if head.direction == "right":
        x = head.xcor()
        motion = 'right'
        if x + 20 <= 250:
            head.setx(x+20)
    #define the snake movement for left
    if head.direction == "left":
        x = head.xcor()
        motion = 'left'
        if x - 20 >= -250:
            head.setx(x-20)
    #define the snake movement for pause
    if head.direction == 'stop':
        motion = 'stop'
        x = head.xcor()
        y = head.ycor()
    #the snake body will expand everytime eats food
    for i in range(9):
        if head.distance(food[i]) < 20:
            food[i].reset()
            food[i].hideturtle()
            food[i].clear()
            number_food -= 1
            length += i + 1
    
    #the game title while playing
    snake_game.tracer(0)
    line.clear()
    line.write("Contact: {0}\t Time: {1} \t Motion: {2}".format(contact, str(int(time.perf_counter())),motion), align="center", font=("Arial", 14, "normal"))
    snake_game.tracer(1)

    #when the monster hit the head the game ends
    if head.distance(monster) < 20:
        end.goto(head.xcor()-20, head.ycor()-30)
        end.write("You dead!", align="left", font=("Arial", 12, "normal"))
        snake = False
        turtle.done()
    
    #when the snake eats all of the food the player wins
    if number_food == 0:
        end.goto(head.xcor()-20, head.ycor()-30)
        end.write("You Win!", align="left", font=("Arial", 12, "normal"))
        snake = False
        turtle.done()
    snake_game.ontimer(head_move, 100)

#define the up direction
def head_up():
    if head.direction != "down":
        head.direction = "up"

#define the down direction
def head_down():
    if head.direction != "up":
        head.direction = "down"

#define the right direction
def head_right():
    if head.direction != "left":
        head.direction = "right"

#define the left direction
def head_left():
    if head.direction != "right":
        head.direction = "left"

#define the pause direction
def head_pause():
    last_direct = ''
    if head.direction != "stop":
        last_direct = head.direction
        head.direction = "stop"
    else:
        head.direction = last_direct

#define the keybind for playing
def set_key():
    snake_game.onkeypress(head_up, key = "Up")
    snake_game.onkeypress(head_down, key = "Down")
    snake_game.onkeypress(head_right, key = "Right")
    snake_game.onkeypress(head_left, key = "Left")
    snake_game.onkeypress(head_pause, key = 'space')
    snake_game.listen()

#define the contact count
contact = 0
def snake_contact():
    global contact, monster, bodys
    for i in range(len(bodys)):
        if monster.distance(bodys[i]) < 30:
            contact += 1

#define the monster movement
def monster_move():
    global snake
    if head.distance(monster) < 20:
        end.goto(head.xcor()-20, head.ycor()-30)
        end.write("You dead!", align="left", font=("Arial", 12, "normal"))
        snake = False
        turtle.done()

    if not snake:
        return

    x = head.xcor() - monster.xcor()
    y = head.ycor() - monster.ycor()
    if x == 0:
        cor_y = monster.ycor()
        if y > 0:
            monster.sety(cor_y + 20)
        else:
            monster.sety(cor_y - 20)
    if y == 0:
        cor_x = monster.xcor()
        if x > 0:
            monster.setx(cor_x + 20)
        else:
            monster.setx(cor_x - 20)
    if x > 0 and y > 0:
        cor_x = monster.xcor()
        cor_y = monster.ycor()
        if x > y:
            monster.setx(cor_x + 20)
        else:
            monster.sety(cor_y + 20)
    elif x > 0 and y < 0:
        cor_x = monster.xcor()
        cor_y = monster.ycor()
        if x > abs(y):
            monster.setx(cor_x + 20)
        else:
            monster.sety(cor_y - 20)
    if x < 0 and y > 0:
        cor_x = monster.xcor()
        cor_y = monster.ycor()
        if abs(x) > y:
            monster.setx(cor_x - 20)
        else:
            monster.sety(cor_y + 20)
    if x < 0 and y < 0:
        cor_x = monster.xcor()
        cor_y = monster.ycor()
        if abs(x) > abs(y):
            monster.setx(cor_x - 20)
        else:
            monster.sety(cor_y - 20)
    snake_contact()
    snake_game.ontimer(monster_move, 400)

food = [None] * 9  
number_food = 9
foodx = []
foody = []
#define the function for generates the food
def generate_food():
    snake_game.tracer(0)
    for i in range(9):
        while True:   #make sure the food does not overlap in x
            x_cor = random.randrange(-230, 230)
            if x_cor not in foodx and not (-30 < x_cor < 30):
                foodx.append(x_cor)
                break
            else:
                continue
        while True:  #make sure the food does not overlap in y
            y_cor = random.randrange(-270, 200)
            if y_cor not in foody and not (-30 < y_cor < 30):
                foody.append(y_cor)
                break
            else:
                continue
        i += 1
    for i in range(9):
        food[i] = turtle.Turtle()
        food[i].penup()
        food[i].speed(0)
        food[i].hideturtle()
        food[i].goto(foodx[i], foody[i])
        food[i].write(i + 1, font=('Arial', 12, "normal"))
    snake_game.tracer(1)

#define the start movement of the game
def game_starter():
    snake_game.onclick(first_page)
    snake_game.ontimer(head_move, 100)
    snake_game.ontimer(monster_move, 400)
    while True:
        snake_game.update()

end = turtle.Turtle()
end.color('red')
end.hideturtle()
end.penup()

#call all of the function
first_page()
snake_game.onclick(click_start)
display()
title()
border()
head_spec()
monster_spec()
set_key()


turtle.mainloop()
