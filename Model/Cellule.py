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
    if type(n) != int:
        return False
    return (n >= 0 and n <= 8) or (n == const.ID_MINE)


def construireCellule (contenu = 0, visible = False):
    if isContenuCorrect(contenu) == False:
        raise ValueError(f"construireCellule : le contenu ({contenu}) n'est pas correct")
    if type(visible) != bool:
        raise TypeError(f"construireCellule : le second paramètre ({type(visible)}) n'est pas un booléen")
    return {const.CONTENU : contenu, const.VISIBLE : visible, const.ANNOTATION: None}


def getContenuCellule(cellule:dict) -> int:
    if type_cellule(cellule) == False :
        raise TypeError("getContenuCellule : Le paramètre n’est pas une cellule.")
    return cellule[const.CONTENU]


def isVisibleCellule(cellule:dict) -> bool:
    if type_cellule(cellule) == False :
        raise TypeError("isVisibleCellule : Le paramètre n’est pas une cellule.")
    return cellule[const.VISIBLE]


def setContenuCellule(cellule:dict,contenu:int) -> None :
    if type(contenu) != int:
        raise TypeError("setContenuCellule : Le second paramètre n’est pas un entier.")
    if not ((contenu >= 0 and contenu <= 8) or (contenu == const.ID_MINE)):
        raise ValueError(f"setContenuCellule : la valeur du contenu ({contenu}) n’est pas correcte.")
    if type_cellule(cellule) == False:
        raise TypeError("setContenuCellule : Le premier paramètre n’est pas une cellule.")
    cellule[const.CONTENU] = contenu
    return None


def setVisibleCellule(cellule: dict, visible: bool) -> None:
    if type_cellule(cellule) == False:
        raise TypeError(" setVisibleCellule : Le premier paramètre n’est pas une cellule.")
    if type(visible) != bool:
        raise TypeError (" setVisibleCellule : Le second paramètre n’est pas un booléen")
    cellule[const.VISIBLE] = visible
    return None


def contientMineCellule(cellule: dict) -> bool:
    if type_cellule(cellule) == False:
        raise TypeError("contientMineCellule : Le paramètre n’est pas une cellule.")
    return cellule[const.CONTENU] == const.ID_MINE


def isAnnotationCorrecte(anno: str) -> bool:
    return anno == None or anno == const.DOUTE or anno == const.FLAG


def getAnnotationCellule(cellule: dict):
    if type_cellule(cellule) == False:
        raise TypeError("getAnnotationCellule : le paramètre valeur_du paramètre n’est pas une cellule")
    if len(cellule) != 3:
        return None
    return cellule[const.ANNOTATION]
