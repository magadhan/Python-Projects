
import turtle
import random 

window = turtle.Screen()
window.bgcolor("black")
start = turtle.Turtle()
start.shape("triangle")
start.speed(0)

def user_star(user = 0):
    '''
    this function stores the number of stars the user wants in the sky
    args: number of stars the user inputs
    return: the number of stars (the integer)
    '''
    user = int(input("How many stars do you want in the sky? Be reasonable. (Choose between 1 - 20)"))
    return user

def line_firework(color = "black", size = 0):
    '''
    this function makes the fireworks with different colors and different sizes
    args: different colors, different sizes later given in the main function
    return: firework shapes made from lines according to the color and size in the function being called
    '''
    xpos = random.randrange(-250, 250)
    ypos = random.randrange(-250, 250)
    start.up()
    for i in range(20):
        start.color(color)
        angle = 180-(360/20)
        start.right(angle)
        start.goto(xpos,ypos)
        start.down()
        start.forward(size)

def stars(star_size  = "0"):
    '''
    this function draws a star according to the star size inputed later
    args: the size of the stars
    return: the star is drawn using lines and angles in the size of the star that is later called
    '''
    start.up()
    xpos = random.randrange(-250, 250)
    ypos = random.randrange(-250, 250)
    start.color("white")
    start.goto(xpos,ypos)
    start.down()
    start.begin_fill()
    for a in range(6):
        start.forward(star_size)
        start.right(115)
        start.forward(star_size)
        start.right(315)
    start.end_fill()

def main():
    star_user = user_star()
    for b in range(star_user):
        stars(star_size = 4)

    fire2 = [40,60,80]
    for c in range(4):
        for fire in fire2:
            line_firework(color = "blue", size = fire)
            line_firework(color = "red", size = fire)
            line_firework(color = "green", size = fire)
    
    window.exitonclick()

main()
