# Model/Cellule.py
#

from Model.Constantes import *

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


def isContenuCorrect(entier : int) -> bool:
    r = False
    if entier == int:
        if (8 >= entier >= 0) or entier == const.ID_MINE():
            r = True
    return r

def construireCellule(contenu:int=0, visibilite:bool=False) -> dict:
    if not (isinstance(contenu, int) and 0 <= contenu <= 9):
        raise ValueError(f"construireCellule : le contenu {contenu} n'est pas correct")
    if not isinstance(visibilite, bool):
        raise TypeError(f"construireCellule : le second paramètre {type(visibilite)} n'est pas un booléen")
    return {contenu,visibilite}