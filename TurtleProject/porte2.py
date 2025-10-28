import turtle

def porte2(x, y, couleur):
    '''
    Paramètres :
        x : abscisse du centre de la porte
        y : ordonnée du sol de la porte
        couleur : couleur de la porte

    Cette fonction dessine une porte dont le haut est un demi-cercle.
    - La porte a une largeur totale de 30 pixels.
    - La partie rectangulaire a une hauteur de 40 pixels.
    - La partie semi-circulaire a un rayon de 15 pixels.
    '''
    turtle.penup()
    # Positionner le coin inférieur gauche du rectangle
    turtle.setposition(x - 15, y)
    turtle.pendown()

    # Définir la couleur de remplissage et tracer
    turtle.pencolor("black")
    turtle.fillcolor(couleur)
    turtle.begin_fill()

    # Dessiner le rectangle
    turtle.setheading(0)  # Orientation vers la droite
    turtle.forward(30)    # Base du rectangle
    turtle.left(90)
    turtle.forward(40)    # Hauteur du rectangle
    turtle.left(90)
    turtle.penup()
    turtle.forward(30)    # Haut du rectangle
    turtle.left(90)
    turtle.pendown()
    turtle.forward(40)    # Retour à la base
    turtle.end_fill()

    # Dessiner le demi-cercle en haut de la porte
    turtle.penup()
    turtle.setposition(x+15, y + 35)  # Centre du demi-cercle
    turtle.setheading(90)    # Orientation à droite
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(15, 180)  # Demi-cercle
    turtle.end_fill()

    turtle.hideturtle()

if __name__ == '__main__':
    turtle.speed(3)  # Vitesse lente pour mieux visualiser le dessin
    porte2(0, 0, "red")
    # Fermer la fenêtre lorsqu'on clique
    turtle.exitonclick()
