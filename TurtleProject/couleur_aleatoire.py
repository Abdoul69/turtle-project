import turtle
from random import randint

def couleur_aleatoire():
    '''
    Renvoie un triplet de 3 nombres entiers compris entre 0 et 255
    Ce triplet correspond à une couleur codée en RVB
    '''
    r = randint(0, 255)  # Composante rouge
    v = randint(0, 255)  # Composante verte
    b = randint(0, 255)  # Composante bleue
    
    # Retourner le triplet RVB
    return (r, v, b)
    



