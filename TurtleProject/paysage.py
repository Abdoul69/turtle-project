import turtle


turtle.bgcolor("skyblue")


def paysage():
    """ fait un paysage derrière les immeubles """
    # Herbe
    turtle.penup()
    turtle.setposition(-400, -200)
    turtle.pendown()
    turtle.color("limegreen")
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(800)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()

    # Montagne Gauche
    turtle.penup()
    turtle.setposition(-450, -200)
    turtle.pendown()
    turtle.color("dimgray")
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(350)
        turtle.left(120)
    turtle.end_fill()

    # Montagne Droite
    turtle.penup()
    turtle.setposition(100, -200)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(400)
        turtle.left(120)
    turtle.end_fill()

    # Montagne Milieu
    turtle.penup()
    turtle.setposition(-260, -200)
    turtle.pendown()
    turtle.color("gray")
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(475)
        turtle.left(120)
    turtle.end_fill()

    # Neige de la Montagne Milieu
    turtle.penup()
    turtle.setposition(-96, 85)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    turtle.left(35)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(100)
    turtle.forward(45)
    turtle.right(85)
    turtle.forward(65)
    turtle.left(160)
    turtle.forward(150)
    turtle.end_fill()

    # Neige de la Montagne Gauche
    turtle.penup()
    turtle.setposition(-240, 45)
    turtle.pendown()
    turtle.color("snow")
    turtle.begin_fill()
    turtle.forward(70)
    turtle.left(120)
    turtle.forward(75)
    turtle.left(150)
    turtle.forward(45)
    turtle.right(90)
    turtle.forward(45)
    turtle.left(120)
    turtle.end_fill()

    # Neige de la Montagne Droite
    turtle.penup()
    turtle.setposition(252, 65)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(95)
    turtle.right(120)
    turtle.forward(80)
    turtle.right(150)
    turtle.forward(50)
    turtle.left(70)
    turtle.end_fill()
    turtle.left(50)

    # Soleil
    turtle.penup()
    turtle.setposition(-500, 320)
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.circle(125)
    turtle.end_fill()
    
    turtle.color("black")
    pass

    
