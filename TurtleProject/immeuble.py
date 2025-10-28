# module immeuble

from couleur_aleatoire import couleur_aleatoire
from random import randint
from rdc import rdc
from etage import etage
from toit import toit
import turtle

def immeuble(x, y_sol):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
    Cette fonction dessine un immeuble Le nombre d'étage est compris aléatoirement entre 0 et 4
    La couleur de la façade et la couleur de la porte sont tirées au hasard
    '''
    turtle.pensize(1)
    # Nombre d'étage (aléatoire)
    niveau = randint(0, 4)
    pass

    #Couleurs des éléments (aléatoire)
    # Obtenir une couleur aléatoire pour l'immeuble
    for k in range(1):
        r, v, b = couleur_aleatoire()

        r_norm = r / 255
        v_norm = v / 255
        b_norm = b / 255
        
        c_immeuble = (r_norm, v_norm, b_norm)
    
    # Obtenir une couleur aléatoire pour les portes
    for k in range(1):
        r, v, b = couleur_aleatoire()

        r_norm = r / 255
        v_norm = v / 255
        b_norm = b / 255
        
        c_porte = (r_norm, v_norm, b_norm) 
    pass

    # Dessin du RDC
    rdc(x, y_sol, c_immeuble, c_porte)
    pass

    # Dessin des étages
    if niveau == 0:
        pass
    else:
        k = 1
        niveau_2 = niveau
        while niveau_2 != 0:
            etage(x, y_sol, c_immeuble, k)
            k += 1
            niveau_2 -= 1
    pass

    # Dessin du toit
    toit(x, y_sol, niveau)
    pass

if __name__ == '__main__':
    immeuble(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()