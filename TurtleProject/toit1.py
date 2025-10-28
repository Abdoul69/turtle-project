import turtle

def toit1(x, y_sol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit triangulaire noir de base 160 pixels
    et de hauteur centrale 40 pixels
    '''
    turtle.pensize(1)
    turtle.penup()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.setposition(x-80, y_sol+60+(60*niveau))
    turtle.pendown()
    turtle.setposition(x+80, y_sol+60+(60*niveau))
    turtle.setposition(x, y_sol + 100 + (60*niveau))
    turtle.setposition(x-80, y_sol+60+(60*niveau))
    turtle.end_fill()
    turtle.hideturtle()
    pass


if __name__ == '__main__':
    toit1(0,0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()