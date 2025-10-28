import turtle


def rectangle(x, y, w, h):
    '''
    Paramètres
        x, y : coordonnées du centre de la base du rectangle
        w : largeur du rectangle
        h : hauteur du rectangle
    Cette fonction dessine un rectangle. Le point (x, y) est
    sur le côté en bas au milieu.
    '''
    turtle.penup()
    turtle.setposition(x - w / 2, y) # Positionner le curseur en bas a gauche du rectangle
    turtle.setheading(90) # Regarder vers le haut
    turtle.pendown()
    
    # Tracer le rectangle en utilisant for...in pour alterner en hauteur et largeur
    for k in (h, w, h, w):
        turtle.forward(k)
        turtle.right(90)

if __name__ == '__main__':
    rectangle(0, 0, 150, 100)
    # Fermer la fenêtre au clic
    turtle.exitonclick()