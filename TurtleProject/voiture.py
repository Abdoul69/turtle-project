import turtle
from roue import roue
from couleur_aleatoire import couleur_aleatoire
from carrosserie import carrosserie

def voiture(x, y):
    
    # Réglages
    turtle.pensize(1)

    # Obtenir une couleur aléatoire pour la voiture
    for k in range(1):
        r, v, b = couleur_aleatoire()
        r_norm = r / 255
        v_norm = v / 255
        b_norm = b / 255
        c_voiture = (r_norm, v_norm, b_norm)
    pass

    # Tracer la carrosserie
    carrosserie(c_voiture, x, y)
    pass

    # Tracer la roue avant
    roue(x, y)
    pass

    # Tracer la roue arrière
    roue(x+115, y)
    pass
    

if __name__ == '__main__':
    turtle.speed(30)  # Vitesse lente pour mieux visualiser le dessin
    voiture(-350, 120)
    # Fermer la fenêtre lorsqu'on clique
    turtle.exitonclick()