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


def isContenuCorrect(n: int) -> bool:
    r = False
    if type(n) == int:
        r = (n >= 0 and n <= 8) or (n == const.ID_MINE)
    return r



def construireCellule (contenu = 0, visibilite = False):
    if type(contenu) != int:
        raise ValueError(f"construireCellule : le contenu ({contenu}) n'est pas correct")
    if type(visibilite) != bool:
        raise TypeError(f"construireCellule : le second paramètre ({type(visibilite)}) n'est pas un booléen")
    return {const.CONTENU : contenu, const.VISIBLE : visibilite}

def getContenuCellule(cellule:dict) -> int:
    if type_cellule(cellule) == False :
        raise TypeError("getContenuCellule : Le paramètre n’est pas une cellule.")
    return cellule[const.CONTENU]

def isVisibleCellule(cellule:dict) -> bool:
    if type_cellule(cellule) == False :
        raise TypeError("isVisibleCellule : Le paramètre n’est pas une cellule.")
    return cellule[const.VISIBLE]


def setContenuCellule(cellule:dict,contenu:int) -> None :
    if type(contenu) == int:
        raise TypeError("setContenuCellule : Le second paramètre n’est pas un entier.")
    if not ((contenu >= 0 and contenu <= 8) or (contenu == const.ID_MINE)):
        raise ValueError(f"setContenuCellule : la valeur du contenu ({contenu}) n’est pas correcte.")
    if type_cellule(cellule) == False:
        raise TypeError("setContenuCellule : Le premier paramètre n’est pas une cellule.")
    cellule[const.CONTENU] = contenu
    return None
