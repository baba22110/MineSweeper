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
    '''
    elle dit si le contenue placer en paramètre est correct
    :param n: le contenue voulant etre verifier
    :return: True si le contenue est bon et False sinon
    '''
    #vérifie le type du contenue si il est différent de int
    if type(n) != int:
        return False
    #retourne True si le contenue est bon et False sinon
    return (n >= 0 and n <= 8) or (n == const.ID_MINE)


def construireCellule (contenu = 0, visible = False) -> dict:
    '''
    elle construie une cellule avec le contenu et la visibiliter passer en paramètre
    :param contenu: le contenue voulue initialiser a 0
    :param visible: la visibiliter de la cellule initialiser a False donc non visible
    :return: la cellule créer
    '''
    # vérifie si le contenu est correct, sinon elle envoie un raise ValueError
    if isContenuCorrect(contenu) == False:
        raise ValueError(f"construireCellule : le contenu ({contenu}) n'est pas correct")
    # vérifie si visible est de bon type, sinon elle envoie un raise TypeError
    if type(visible) != bool:
        raise TypeError(f"construireCellule : le second paramètre ({type(visible)}) n'est pas un booléen")
    # retourne la cellule
    return {const.CONTENU: contenu, const.VISIBLE: visible, const.ANNOTATION: None}


def getContenuCellule(cellule:dict) -> int:
    '''
    elle retourne le contenue de la cellule
    :param cellule: la cellule
    :return: le contenue
    '''
    if type_cellule(cellule) == False :
        raise TypeError("getContenuCellule : Le paramètre n’est pas une cellule.")
    return cellule[const.CONTENU]


def isVisibleCellule(cellule:dict) -> bool:
    '''
    renvoie la visibiliter de la cellule passer en paramètre
    :param cellule: la cellule voulue
    :return: la visibiliiter, True si visible, False sinon
    '''
    if type_cellule(cellule) == False :
        raise TypeError("isVisibleCellule : Le paramètre n’est pas une cellule.")
    return cellule[const.VISIBLE]


def setContenuCellule(cellule:dict,contenu:int) -> None :
    '''
    change le contenue de la cellule placer en paramètre par le contenu
    :param cellule: la cellule voulue
    :param contenu: le contenue
    :return: rien
    '''
    if type(contenu) != int:
        raise TypeError("setContenuCellule : Le second paramètre n’est pas un entier.")
    if not ((contenu >= 0 and contenu <= 8) or (contenu == const.ID_MINE)):
        raise ValueError(f"setContenuCellule : la valeur du contenu ({contenu}) n’est pas correcte.")
    if type_cellule(cellule) == False:
        raise TypeError("setContenuCellule : Le premier paramètre n’est pas une cellule.")
    cellule[const.CONTENU] = contenu
    return None


def setVisibleCellule(cellule: dict, visible: bool) -> None:
    '''
    change la visibiliter de la cellule voulue
    :param cellule: la cellule voulue
    :param visible: la visibiliter voulue de la cellule
    :return: rien
    '''
    if type_cellule(cellule) == False:
        raise TypeError(" setVisibleCellule : Le premier paramètre n’est pas une cellule.")
    if type(visible) != bool:
        raise TypeError (" setVisibleCellule : Le second paramètre n’est pas un booléen")
    cellule[const.VISIBLE] = visible
    return None


def contientMineCellule(cellule: dict) -> bool:
    '''
    envoie si la cellule contient une mine ou non
    :param cellule: la cellule
    :return: True si la cellule contient une mine, False sinon
    '''
    if type_cellule(cellule) == False:
        raise TypeError("contientMineCellule : Le paramètre n’est pas une cellule.")
    return cellule[const.CONTENU] == const.ID_MINE


def isAnnotationCorrecte(anno: str) -> bool:
    '''
    verifie si l'annotation passer en paramètre est bonne ou non
    :param anno: l'annotation voulue
    :return: True si l'annotation est bonne, False sinon
    '''
    return anno == None or anno == const.DOUTE or anno == const.FLAG


def getAnnotationCellule(cellule: dict):

    if type_cellule(cellule) == False:
        raise TypeError("getAnnotationCellule : le paramètre valeur_du paramètre n’est pas une cellule")
    if len(cellule) != 3:
        return None
    return cellule[const.ANNOTATION]


def changeAnnotationCellule(cellule: dict) -> None:
    if type_cellule(cellule) == False:
        raise TypeError("changeAnnotationCellule : le paramètre n’est pas une cellule")
    anno = getAnnotationCellule(cellule)
    if isVisibleCellule(cellule) == False:
        if anno == None:
            cellule[const.ANNOTATION] = const.FLAG
        elif anno == const.FLAG:
            cellule[const.ANNOTATION] = const.DOUTE
        if anno == const.DOUTE:
            cellule[const.ANNOTATION] = None
    return None


def reinitialiserCellule(cellule: dict) -> None:
    setContenuCellule(cellule,0)
    setVisibleCellule(cellule,False)
    while getAnnotationCellule(cellule) != None:
        changeAnnotationCellule(cellule)
    return None