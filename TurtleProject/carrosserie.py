import turtle

def carrosserie(couleur, x, y):

    # Positionner le coin inférieur gauche de la voiture
    turtle.hideturtle()
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()

    # Définir la couleur de remplissage et tracer
    turtle.pencolor("black")
    turtle.fillcolor(couleur)
    turtle.begin_fill()

    # Bas de la voiture
    turtle.forward(210)

    # Arrière de la voiture
    turtle.left(80)
    turtle.forward(45)
    turtle.left(95)
    turtle.forward(40)

    # Toit de la voiture
    turtle.right(45)
    turtle.forward(35)
    turtle.left(50)
    turtle.forward(80)
    turtle.left(55)
    turtle.forward(35)

    # Avant de la voiture
    turtle.right(45)
    turtle.forward(50)
    turtle.left(70)
    turtle.forward(39)
    turtle.end_fill()

    # Porte Avant
    xy_porte_avant = (x+60, y+5)
    turtle.penup()
    turtle.setposition(xy_porte_avant)
    turtle.right(170)
    turtle.pendown()
    
    for i in range(2):
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(55)
        turtle.right(90)

    xy_vitre_avant = (x+115, y+45)
    turtle.penup()
    turtle.setposition(xy_vitre_avant)
    turtle.pendown()
    turtle.fillcolor("grey70")
    turtle.begin_fill()
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(38)
    turtle.left(55)
    turtle.forward(30)
    turtle.end_fill()

    # Porte Arrière
    xy_porte_arriere = (x+120, y+5)
    turtle.penup()
    turtle.setposition(xy_porte_arriere)
    turtle.left(215)
    turtle.pendown()
    
    for i in range(2):
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(55)
        turtle.right(90)

    xy_vitre_arriere = (x+120, y+45)
    turtle.penup()
    turtle.setposition(xy_vitre_arriere)
    turtle.pendown()
    turtle.fillcolor("grey70")
    turtle.begin_fill()
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(34)
    turtle.right(50)
    turtle.forward(33)
    turtle.end_fill()

    # Phare Avant
    xy_phare_avant = (x+6, y+35)
    turtle.penup()
    turtle.setposition(xy_phare_avant)
    turtle.left(55)
    turtle.pendown()
    turtle.fillcolor("DarkOrange2")
    turtle.begin_fill()
    turtle.forward(15)
    turtle.right(95)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(100)
    turtle.forward(10)
    turtle.end_fill()

    # Phare Arrière
    xy_phare_arriere = (x+212, y+25)
    turtle.penup()
    turtle.setposition(xy_phare_arriere)
    turtle.left(100)
    turtle.pendown()
    turtle.fillcolor("red3")
    turtle.begin_fill()
    turtle.forward(10)
    turtle.right(95)
    turtle.forward(17)
    turtle.right(95)
    turtle.forward(12)
    turtle.right(90)
    turtle.forward(15)
    turtle.end_fill()
    pass  