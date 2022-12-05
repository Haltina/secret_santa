from random import *

## fonctions python pour secret Santa

## liste des collègues doublé pour un donneur qui va offir à un receveur  
donneur = ["Collègue 1", "Collègue 2", "Collègue 3", "Collègue 4", "Collègue 5"]
receveur = ["Collègue 1", "Collègue 2", "Collègue 3", "Collègue 4", "Collègue 5"]

while len(donneur) >= 1:
    personne1 = donneur[0]
    personne2 = personne1
    while personne1 == personne2:
        personne2 = receveur[randint(0, len(receveur) - 1)]
    print(personne1 + " offre un cadeau à " + personne2)
    donneur.remove(personne1)
    receveur.remove(personne2)
