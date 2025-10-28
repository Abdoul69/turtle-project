import turtle
from rectangle import rectangle
from trait import trait

def fenetre_balcon(x,y):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte-fenetre-balcon
        y est l'ordonnée du sol du niveau de la porte-fenetre-balcon
    Remarque:
        Dessine une porte-fenetre avec balcon en 2 temps: la porte fenetre de 30 pixels de large par 50 pixels de hauteur
        puis le balcon
    '''
    # porte-fenetre
    turtle.fillcolor('white')
    turtle.begin_fill()
    rectangle(x, y, 30, 50)
    turtle.end_fill()
    pass
    # balcon
    turtle.pensize(3)
    rectangle(x, y, 40, 25)  # Le balcon est placé juste au-dessus de la porte (hauteur 10)
    turtle.penup()
    turtle.setposition(x-15, y)
    turtle.pendown
    recul = -15
    for k in range(7):
        trait((x+recul), y, (x+recul), y+25)
        recul = recul + 5 
    turtle.pensize(1)
    pass



if __name__ == '__main__':
    fenetre_balcon(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()