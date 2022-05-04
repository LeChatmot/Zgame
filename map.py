import random


def generer_terrain():
    grille = [[random.randint(0,3) for _ in range(10)] for _ in range(10)]

    return grille

def add_mer(grille,cote1,coté2=0):
    if coté2 == 0:
        if cote1 == 1:
            # TODO
            pass
        elif cote1 == 2:
            # TODO
            pass
        elif cote1 == 3:
            # TODO
            pass
        else:
            # TODO
            pass
    else:
        #TODO
        pass

    return grille


print(generer_terrain())