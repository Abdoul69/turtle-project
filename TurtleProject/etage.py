from facade import facade
from random import shuffle,randint
from fenetre import fenetre
from rdc import rdc
from fenetre_balcon import fenetre_balcon
import turtle

def etage(x, y_sol, couleur, niveau):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade de l'étage
        niveau : numéro de l'étage en partant de 0 pour le rdc
    Remarque
       Cette fonction dessine un étage d'un immeuble
    '''
    # dessin des murs
    if niveau >= 5:
        return
    if niveau == 0:
        return
    else:
        facade(x, y_sol, couleur, niveau)
    # dessin des 3 Eléments
    liste = [fenetre_balcon, fenetre]
    shuffle(liste)
    if liste[randint(0, 1)] == fenetre_balcon:
        fenetre_balcon(x-40, y_sol+(60*niveau))        
    else:
        fenetre(x-40, (y_sol+20)+(60*niveau))
        
    if liste[randint(0, 1)] == fenetre_balcon:
        fenetre_balcon(x, y_sol+(60*niveau))        
    else:
        fenetre(x, (y_sol+20)+(60*niveau))
    
    if liste[randint(0, 1)] == fenetre_balcon:
        fenetre_balcon(x + 40, y_sol+(60*niveau))        
    else:
        fenetre(x + 40, (y_sol+20)+(60*niveau)) 
    
    turtle.hideturtle()
            
    pass

if __name__ == '__main__':
    etage(0,0,"blue",2)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()