# Model/Cellule.py
#

import const
from Model.Constantes import *
from Model.Coordonnee import *
#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)

def isContenuCorrect(n : int) -> bool:
    r = False
    if type(n) == int:
        r = (n >= 0 and n <= 8) or (n == const.ID_MINE)
    return r


def construireCellule(contenu=0, visibilite=False) -> dict:
    if type(contenu) != int:
        raise ValueError(f"construireCellule : le contenu {contenu} n'est pas correct")
    if type(visibilite) != bool:
        raise TypeError(f"construireCellule : le second paramètre {type(visibilite)} n'est pas un booléen")
    return {contenu:visibilite}
