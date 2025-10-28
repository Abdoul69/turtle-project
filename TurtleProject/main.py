import turtle
from random import randint, shuffle
from sol import sol
from immeuble import immeuble
from paysage import paysage
from voiture import voiture
from route import route
from trait import trait



def main():
    # Réglages pour l'affichage et la vitesse de dessin
    turtle.setup(800, 600)
    turtle.speed(15000)

    # Dessin du paysage
    paysage()

    # On définit la hauteur du sol
    y_sol = -200

    # Dessin du sol de la rue
    sol(y_sol)

    # Dessin des 4 immeubles
    immeuble(-260, y_sol)
    immeuble(-90, y_sol)
    immeuble(80, y_sol)
    immeuble(250, y_sol)
    
    #Dessiner la route
    turtle.pensize(2)
    trait(-400, -220, 400, -220)
    turtle.pensize(1)
    route()
    
    
    # Remettre droit et dessiner la voiture
    turtle.right(90)
    voiture(170, -280)
    

    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()

if __name__ == '__main__':
    main()