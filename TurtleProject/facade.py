import turtle
from rectangle import rectangle

def facade(x, y_sol, couleur, niveau):
    '''
    Paramètres :
        x : abcisse du centre de la façade
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade
        niveau : num du niveau (0 pour les rdc, ...)
    remarque :
        Facade dessine une facade sans les élements interieurs
    '''
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    if niveau == 0:
        rectangle(x, y_sol, 140, 60)
    elif niveau == 1:
        rectangle(x, y_sol + 60, 140, 60)
    elif niveau == 2:
        rectangle(x, y_sol + 120, 140, 60)
    elif niveau == 3:
        rectangle(x, y_sol + 180, 140, 60)
    elif niveau == 4:
        rectangle(x, y_sol + 240, 140, 60)
       
    turtle.end_fill()

    pass

if __name__ == '__main__':
    facade(0,0,"red",4)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()