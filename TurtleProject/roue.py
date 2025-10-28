import turtle

def roue(x, y):

    # Trouver les coordonnées et tracer la pneu
    x_pneu = x+35
    y_pneu = y+5
    # Se positionner
    turtle.penup()
    turtle.setposition(x_pneu, y_pneu)
    turtle.pendown()
    # Définir la couleur de remplissage et tracer
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

    # Trouver les coordonnées et tracer la jante avant
    x_jante = x+40
    y_jante = y+5
    # Se positionner
    turtle.penup()
    turtle.setposition(x_jante, y_jante)
    turtle.pendown()
    turtle.fillcolor("grey70")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()
    pass