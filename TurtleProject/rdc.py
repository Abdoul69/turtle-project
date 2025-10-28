from facade import facade
from random import shuffle, randint
from porte import porte
from porte2 import porte2
from fenetre import fenetre
import turtle

def rdc(x, y_sol, c_facade, c_porte):
    '''
    Paramètres
        x : (int) abscisse du centre
        y_sol : ordonnée du sol du la rue
        c_facade : couleur de la façade
        c_porte : couleur de la porte
    remarque:
        Cette fonction dessine le rdc en 2 étapes
        D'abord la façade
        Puis les 3 élements : 1 porte et 2 fenêtres disposées au hasard
    '''
    # Dessine la facade
    facade(x, y_sol, c_facade, 0)
    pass
    
    # Construit les 3 éléments (1 porte et 2 fenetres)
    liste = [fenetre,porte,fenetre]
    shuffle(liste)
    if liste[0] == porte:
        test_porte = randint(1, 2)
        if test_porte == 1:
            porte(x-40, y_sol, c_porte)
        else:
            porte2(x-40, y_sol, c_porte)
        turtle.penup()
        turtle.setposition(x, y_sol +20)
        turtle.pendown
        fenetre(x, y_sol + 20)
        turtle.penup()
        turtle.setposition(x+40, y_sol +20)
        turtle.pendown
        fenetre(x+40, y_sol + 20)
    else:
        turtle.fillcolor('white')
        turtle.begin_fill()
        fenetre(x-40, y_sol + 20)
        turtle.end_fill()
        if liste[1] == porte:
            test_porte = randint(1, 2)
            if test_porte == 1:
                porte(x, y_sol, c_porte)
            else:
                porte2(x, y_sol, c_porte)
            turtle.penup()
            turtle.setposition(x+40, y_sol +20)
            turtle.pendown
            fenetre(x+40, y_sol + 20)

        else:
            turtle.penup()
            turtle.setposition(x, y_sol +20)
            turtle.pendown
            fenetre(x, y_sol + 20)
            test_porte = randint(1, 2)
            if test_porte == 1:
                porte(x+40, y_sol, c_porte)
            else:
                porte2(x+40, y_sol, c_porte)  
    pass

if __name__ == '__main__':
    rdc(0,0,"red","green")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()