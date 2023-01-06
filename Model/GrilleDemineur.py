# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse
from random import *


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                                         and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True


def construireGrilleDemineur(nb_ligne: int, nb_colonnes: int) -> list:
    if type(nb_ligne) != int or type(nb_colonnes) != int:
        raise TypeError(
            f"construireGrilleDemineur : Le nombre de lignes ({nb_ligne}) ou de colonnes ({nb_colonnes}) n’est pas un entier.")
    if nb_ligne <= 0 or nb_colonnes <= 0:
        raise ValueError(
            f" construireGrilleDemineur : Le nombre de lignes ({nb_ligne}) ou de colonnes ({nb_colonnes}) est négatif ou nul.")
    grille = []
    for i in range(nb_ligne):
        col = []
        for j in range(nb_colonnes):
            col.append(construireCellule())
        grille.append(col)
    return grille


def getNbLignesGrilleDemineur(grille: list) -> int:
    if type_grille_demineur(grille) == False:
        raise TypeError("getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(grille)


def getNbColonnesGrilleDemineur(grille: list) -> int:
    if type_grille_demineur(grille) == False:
        raise TypeError("getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(grille[0])


def isCoordonneeCorrecte(grille: list, coord: tuple) -> bool:
    if type_grille_demineur(grille) == False or type(coord) != tuple:
        raise TypeError("isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")
    return getNbLignesGrilleDemineur(grille) > coord[0] and getNbColonnesGrilleDemineur(grille) > coord[1] and coord[
        0] >= 0 and coord[1] >= 0


def getCelluleGrilleDemineur(grille: list, coord: tuple) -> dict:
    if type_grille_demineur(grille) == False or type_coordonnee(coord) == False:
        raise TypeError("getCelluleGrilleDemineur : un des paramètres n’est pas du bon type")
    if isCoordonneeCorrecte(grille, coord) == False:
        raise IndexError("getCelluleGrilleDemineur : coordonnée non contenue dans la grille.")
    return grille[coord[0]][coord[1]]


def getContenuGrilleDemineur(grille: list, coord: tuple) -> int:
    return getContenuCellule(getCelluleGrilleDemineur(grille, coord))


def setContenuGrilleDemineur(grille: list, coord: tuple, contenu: int) -> bool:
    setContenuCellule(getCelluleGrilleDemineur(grille, coord), contenu)
    return None


def isVisibleGrilleDemineur(grille: list, coord: tuple) -> bool:
    return isVisibleCellule(getCelluleGrilleDemineur(grille, coord))


def setVisibleGrilleDemineur(grille: list, coord: tuple, visible: bool) -> None:
    setVisibleCellule(getCelluleGrilleDemineur(grille, coord), visible)
    return None


def contientMineGrilleDemineur(grille: list, coord: tuple) -> bool:
    return getContenuCellule(getCelluleGrilleDemineur(grille, coord)) == const.ID_MINE


def getCoordonneeVoisinsGrilleDemineur(grille: list, coord: tuple) -> list:
    if type_grille_demineur(grille) == False or type(coord) != tuple:
        raise TypeError("getCoordonneeVoisinsGrilleDemineur : un des paramètres n’est pas du bon type.")

    if isCoordonneeCorrecte(grille, coord) == False:
        raise IndexError("getCoordonneeVoisinsGrilleDemineur : la coordonnée n’est pas dans la grille.")

    l_coord = coord[0]
    c_coord = coord[1]
    cell_voisines = []
    voisins = [(l_coord - 1, c_coord - 1), (l_coord - 1, c_coord), (l_coord - 1, c_coord + 1), (l_coord, c_coord - 1),
               (l_coord, c_coord + 1), (l_coord + 1, c_coord - 1), (l_coord + 1, c_coord),
               (l_coord + 1, c_coord + 1)]
    for co_voisine in voisins:
        if isCoordonneeCorrecte(grille, co_voisine) == True:
            cell_voisines.append(co_voisine)
    return cell_voisines


def placerMinesGrilleDemineur(grille: list, nb_mine: int, coord: tuple) -> None:
    nb_col = getNbColonnesGrilleDemineur(grille)
    nb_lig = getNbLignesGrilleDemineur(grille)
    if nb_mine < 0 or nb_mine >= (nb_lig * nb_col):
        raise ValueError("placerMinesGrilleDemineur : Nombre de bombes à placer incorrect")
    if isCoordonneeCorrecte(grille, coord) == False:
        raise IndexError("placerMinesGrilleDemineur : la coordonnée n’est pas dans la grille.")
    if type_grille_demineur(grille) == False:
        raise TypeError("placerMinesGrilleDemineur : le premiers paramètres n’est pas du bon type.")

    while nb_mine > 0:
        co_mine = (randint(0, nb_lig), randint(0, nb_col))
        if isCoordonneeCorrecte(grille, co_mine) == True and getContenuGrilleDemineur(grille, co_mine) != const.ID_MINE and co_mine != coord:
            setContenuGrilleDemineur(grille, co_mine, const.ID_MINE)
        else:
            nb_mine += 1
        nb_mine -= 1
    compterMinesVoisinesGrilleDemineur(grille)
    return None


def compterMinesVoisinesGrilleDemineur(grille: list) -> None:
    if type_grille_demineur(grille) == False:
        raise TypeError("compterMinesVoisinesGrilleDemineur : le premiers paramètres n’est pas du bon type.")
    nb_col = getNbColonnesGrilleDemineur(grille)
    nb_lig = getNbLignesGrilleDemineur(grille)
    for j in range(nb_lig):
        for i in range(nb_col):
            co = (j, i)
            if getContenuGrilleDemineur(grille, co) != const.ID_MINE:
                nb_mine = 0
                co_voisine = getCoordonneeVoisinsGrilleDemineur(grille, (j, i))
                for z in co_voisine:
                    if getContenuGrilleDemineur(grille, z) == const.ID_MINE:
                        nb_mine += 1
                setContenuGrilleDemineur(grille, co, nb_mine)
    return None

def getNbMinesGrilleDemineur(grille: list) -> int:
    if type_grille_demineur(grille) == False:
        raise ValueError("getNbMinesGrilleDemineur : le paramètre n’est pas une grille.")
    nb_col = getNbColonnesGrilleDemineur(grille)
    nb_lig = getNbLignesGrilleDemineur(grille)
    nb_mine =0
    for j in range(nb_lig):
        for i in range(nb_col):
            co = (j, i)
            if getContenuGrilleDemineur(grille, co) == const.ID_MINE:
                nb_mine += 1
    return nb_mine


def getAnnotationGrilleDemineur(grille: list, coord: tuple):
    return getAnnotationCellule(getCelluleGrilleDemineur(grille, coord))


def getMinesRestantesGrilleDemineur(grille: list) -> int:
    nb_col = getNbColonnesGrilleDemineur(grille)
    nb_lig = getNbLignesGrilleDemineur(grille)
    nb = 0
    for j in range(nb_lig):
        for i in range(nb_col):
            co = (j, i)
            if getAnnotationGrilleDemineur(grille, co) == const.FLAG:
                nb += 1
    return getNbMinesGrilleDemineur(grille) - nb


def gagneGrilleDemineur(grille: list) -> bool:
    if type_grille_demineur(grille) == False:
        raise ValueError("gagneGrilleDemineur : le paramètre n’est pas une grille.")
    nb_col = getNbColonnesGrilleDemineur(grille)
    nb_lig = getNbLignesGrilleDemineur(grille)
    for j in range(nb_lig):
        for i in range(nb_col):
            co = (j, i)
            if (isVisibleCellule(getCelluleGrilleDemineur(grille, co)) == False and getContenuGrilleDemineur(grille, co) != const.ID_MINE) or (isVisibleCellule(getCelluleGrilleDemineur(grille, co)) == True and getContenuGrilleDemineur(grille, co) == const.ID_MINE):
                return False
    return True

