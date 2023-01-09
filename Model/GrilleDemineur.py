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
    '''
    creer une grille avec de nombre de ligne voulue et le nombre de colonnes voulue 
    :param nb_ligne: le nombre de ligne voulue
    :param nb_colonnes: le nombre de colonnes voulue 
    :return:
    '''
    # Si le type de nb_ligne ou de nb_colonnes n'est pas un entier, lever une exception TypeError
    if type(nb_ligne) != int or type(nb_colonnes) != int:
        raise TypeError(
            f"construireGrilleDemineur : Le nombre de lignes ({nb_ligne}) ou de colonnes ({nb_colonnes}) n’est pas un entier.")
    # Si nb_ligne ou nb_colonnes est négatif ou nul, lever une exception ValueError
    if nb_ligne <= 0 or nb_colonnes <= 0:
        raise ValueError(
            f" construireGrilleDemineur : Le nombre de lignes ({nb_ligne}) ou de colonnes ({nb_colonnes}) est négatif ou nul.")

    # Initialiser une liste vide pour stocker la grille
    grille = []
    # Pour chaque ligne de la grille
    for i in range(nb_ligne):
        # Initialiser une liste vide pour stocker les colonnes de la ligne actuelle
        col = []
        # Pour chaque colonne de la ligne actuelle
        for j in range(nb_colonnes):
            # Ajouter une cellule à la liste des colonnes
            col.append(construireCellule())
        # Ajouter les colonnes de la ligne actuelle à la grille
        grille.append(col)

    # Retourner la grille
    return grille


def getNbLignesGrilleDemineur(grille: list) -> int:
    '''
    dit le nombre de ligne de la grille passez en paramètre
    :param grille: la grille
    :return: le nombre de ligne de la grille
    '''
    if type_grille_demineur(grille) == False:
        raise TypeError("getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(grille)


def getNbColonnesGrilleDemineur(grille: list) -> int:
    '''
    dit le nombre de colonnes de la grille passez en paramètre
    :param grille: la grille
    :return: le nombre de colonnes de la grille
    '''
    if type_grille_demineur(grille) == False:
        raise TypeError("getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(grille[0])


def isCoordonneeCorrecte(grille: list, coord: tuple) -> bool:
    '''
    vérifie si les coordonnées passez en paramètre sont dans la grille
    :param grille: la grille
    :param coord: les coordonnées
    :return: True si les coordonnées sont dans la grille, False sinon
    '''
    if type_grille_demineur(grille) == False or type(coord) != tuple:
        raise TypeError("isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")
    return getNbLignesGrilleDemineur(grille) > coord[0] and getNbColonnesGrilleDemineur(grille) > coord[1] and coord[
        0] >= 0 and coord[1] >= 0


def getCelluleGrilleDemineur(grille: list, coord: tuple) -> dict:
    '''
    envoie la cellule de la grille de coordonnée
    :param grille: la grille
    :param coord: la coordonnée
    :return: la cellule de coordonnée coord dans la grille
    '''
    if type_grille_demineur(grille) == False or type_coordonnee(coord) == False:
        raise TypeError("getCelluleGrilleDemineur : un des paramètres n’est pas du bon type")
    if isCoordonneeCorrecte(grille, coord) == False:
        raise IndexError("getCelluleGrilleDemineur : coordonnée non contenue dans la grille.")
    return grille[coord[0]][coord[1]]


def getContenuGrilleDemineur(grille: list, coord: tuple) -> int:
    '''
    envoie le contenue de la cellule au coordonnée passez en paramètre
    :param grille: la grille
    :param coord: la coordonnée
    :return: le contenue de la cellule au coordonnée coord
    '''
    return getContenuCellule(getCelluleGrilleDemineur(grille, coord))


def setContenuGrilleDemineur(grille: list, coord: tuple, contenu: int) -> bool:
    '''
    change le contenue de la cellule au coordonnée passez en paramètre par le contenue passez en paramètre
    :param grille: la grille
    :param coord: la coordonnée
    :param contenu: le contenue
    :return: rien
    '''
    setContenuCellule(getCelluleGrilleDemineur(grille, coord), contenu)
    return None


def isVisibleGrilleDemineur(grille: list, coord: tuple) -> bool:
    '''
    envoie la visibiliter de la cellule au coordonnée passez en paramètre
    :param grille: la grille
    :param coord: la coordonnées
    :return: la visibilité de la cellule
    '''
    return isVisibleCellule(getCelluleGrilleDemineur(grille, coord))


def setVisibleGrilleDemineur(grille: list, coord: tuple, visible: bool) -> None:
    '''
    change la visibilité de la cellule au coordonnée coord par la visibilité donnez en paramètre
    :param grille: la grille
    :param coord: la coordonnée
    :param visible: la visibilité voulue
    :return: rien
    '''
    setVisibleCellule(getCelluleGrilleDemineur(grille, coord), visible)
    return None


def contientMineGrilleDemineur(grille: list, coord: tuple) -> bool:
    '''
    verifie si la cellule au coordonnée passez en paramètre contient une mine
    :param grille: la grille
    :param coord: la coordonnée
    :return: True si la cellule contient une mine, False sinon
    '''
    return getContenuCellule(getCelluleGrilleDemineur(grille, coord)) == const.ID_MINE


def getCoordonneeVoisinsGrilleDemineur(grille: list, coord: tuple) -> list:
    '''
    recherche toute les coordonnées des voisins de la cellules au coordonnées placez en paramètre
    :param grille: la grille
    :param coord: la coordonnée
    :return: une liste avec toute les coordonnées des cellules voisines
    '''
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
    '''
    placer le nombre de mine voulue passez en paramètre dans la grille sauf au coordonnée coord
    :param grille: la grille
    :param nb_mine: le nombre de mines voulue
    :param coord: la coordonnée
    :return: rien
    '''
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
    '''
    elle compte le nombre de mines voisines pour chaque cellule de la grille passez en paramètre, elle change le contenue de la cellule par le nombre de mine autour d'elle
    :param grille: la grille
    :return: rien
    '''
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
    '''
    elle renvoie le nombre de mine de la grille
    :param grille: la grille
    :return: le nombre de mine de la grille
    '''
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
    '''
    change l'annotation de la cellule au coordonnée passez en paramètre
    :param grille: la grille
    :param coord: la coordonnée
    :return: change l'annotation de la cellule
    '''
    return getAnnotationCellule(getCelluleGrilleDemineur(grille, coord))


def getMinesRestantesGrilleDemineur(grille: list) -> int:
    '''
    compte le nombre de mine restante de la grille passez en paramètre
    :param grille: la grille
    :return: le nombre de mine restante de la grille en retirants le nombre de drapeau placer
    '''
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
    '''
    envoie si la partie est gagner ou non
    :param grille: la grille
    :return: True si la partie est gagner, False sinon
    '''
    if type_grille_demineur(grille) == False:
        raise ValueError("gagneGrilleDemineur : le paramètre n’est pas une grille.")
    nb_col = getNbColonnesGrilleDemineur(grille)
    nb_lig = getNbLignesGrilleDemineur(grille)
    for j in range(nb_lig):
        for i in range(nb_col):
            co = (j, i)
            if (isVisibleCellule(getCelluleGrilleDemineur(grille, co)) == False and getContenuGrilleDemineur(grille, co) != const.ID_MINE) or (isVisibleCellule(getCelluleGrilleDemineur(grille, co)) == True and getContenuGrilleDemineur(grille, co) == const.ID_MINE) or getMinesRestantesGrilleDemineur(grille) > 0:
                return False
    return True


def perduGrilleDemineur(grille: list) -> bool:
    '''
    envoie si la partie est perdu
    :param grille: la grille
    :return: True si la partie est perdu donc qu'une mine est visible, False sinon
    '''
    if type_grille_demineur(grille) == False:
        raise ValueError("perduGrilleDemineur : le paramètre n’est pas une grille.")
    nb_col = getNbColonnesGrilleDemineur(grille)
    nb_lig = getNbLignesGrilleDemineur(grille)
    for j in range(nb_lig):
        for i in range(nb_col):
            co = (j, i)
            if isVisibleCellule(getCelluleGrilleDemineur(grille, co)) == True and getContenuGrilleDemineur(grille, co) == const.ID_MINE:
                return True
    return False


def reinitialiserGrilleDemineur(grille: list) -> None:
    '''
    reinitialise toute la grille passez en paramètre
    :param grille: la grille
    :return: rien
    '''
    nb_col = getNbColonnesGrilleDemineur(grille)
    nb_lig = getNbLignesGrilleDemineur(grille)
    for j in range(nb_lig):
        for i in range(nb_col):
            co = (j, i)
            reinitialiserCellule(getCelluleGrilleDemineur(grille,co))
    return None


def decouvrirGrilleDemineur(grille: list, coord: tuple) -> set:
    '''
    decouvre une partie de la grille si une cellule n'a pas mine autour elle decouvre les cellules autour
    :param grille: la grille
    :param coord: la coordonnée de la cellule
    :return: l'ensemble des coordonnées des cellules découvertes
    '''
    co_decouvert = []
    co_decouvert.append(coord)
    cell_a_explorer = []
    cell_a_explorer.append(coord)
    i = 0
    while len(cell_a_explorer)>i:
        if getContenuCellule(getCelluleGrilleDemineur(grille, cell_a_explorer[i])) == 0:
            cell_voisine = getCoordonneeVoisinsGrilleDemineur(grille, cell_a_explorer[i])
            for j in cell_voisine:
                if not(j in co_decouvert):
                    co_decouvert.append(j)
                if getContenuCellule(getCelluleGrilleDemineur(grille, j)) == 0 and not(j in cell_a_explorer) and isVisibleCellule(getCelluleGrilleDemineur(grille,j)) == False:
                    cell_a_explorer.append(j)
        i += 1
    return set(co_decouvert)


def simplifierGrilleDemineur(grille: list, coord: tuple) -> set:
    '''
    la fonction compte le nombre de drapeaux dans le voisinage de cette case. Si ce nombre
    correspond exactement au contenu de la case, la fonction rend toutes les autres cases voisines
    visibles. On relance alors le procédé sur les cases rendues visibles
    :param grille: la grille
    :param coord: la coordonnée
    :return: l’ensemble des coordonnées des cases rendues visibles
    '''
    resultat = []
    cellule = getCelluleGrilleDemineur(grille, coord)
    if isVisibleCellule(cellule) == True:
        voisins = getCoordonneeVoisinsGrilleDemineur(grille, coord)
        nb_drapeau = 0
        for co_voisines in voisins:
            cell_voisines = getCelluleGrilleDemineur(grille, co_voisines)
            if getAnnotationCellule(cell_voisines) == const.FLAG:
                nb_drapeau += 1
        if nb_drapeau == getContenuCellule(cellule):
            for co_voisines in voisins:
                cell_voisines = getCelluleGrilleDemineur(grille, co_voisines)
                if getAnnotationGrilleDemineur(grille, co_voisines) == None and isVisibleCellule(cell_voisines) == False:
                    resultat.append(co_voisines)
    return set(resultat)


def ajouterFlagsGrilleDemineur(grille: list, coord: tuple) -> set:
    '''
    Si le contenu de la cellule correspond au nombre de cases non découvertes dans le voisinage, alors la
    fonction place un drapeau sur celles qui n’en n’ont pas.
    :param grille: la grille
    :param coord: la coordonnée
    :return: l’ensemble des coordonnées des cellules sur lesquelles elle a placé un drapeau
    '''
    resultat = []
    cellule = getCelluleGrilleDemineur(grille, coord)
    voisins = getCoordonneeVoisinsGrilleDemineur(grille, coord)
    nb_cell = 0
    for co_voisines in voisins:
        cell_voisines = getCelluleGrilleDemineur(grille, co_voisines)
        if isVisibleCellule(cell_voisines) == False:
            nb_cell += 1
    if nb_cell == getContenuCellule(cellule):
        for co_voisines in voisins:
            cell_voisines = getCelluleGrilleDemineur(grille, co_voisines)
            if isVisibleCellule(cell_voisines) == False and getAnnotationCellule(cell_voisines) == None:
                changeAnnotationCellule(cell_voisines)
                resultat.append(co_voisines)
    return set(resultat)


def simplifierToutGrilleDemineur(grille: list) -> tuple:
    '''
    cette fonction utilise ajouterFlagsGrilleDemineur et simplifierGrilleDemineur pour simplifier au maximum la grille passez en paramètre
    :param grille: la grille
    :return: un tuple contenant en premier l’ensemble des coordonnées des cellules rendues visible
    et en second l’ensemble des coordonnées des cellules sur lesquelles a été ajouté un drapeau
    '''
    cell_deja_faite = []
    nb_col = getNbColonnesGrilleDemineur(grille)
    nb_lig = getNbLignesGrilleDemineur(grille)
    modif = 1
    coord_ajout_drapeau = []
    coord_rendue_visible = []
    while modif > 0:
        modif = 0
        for j in range(nb_lig):
            for i in range(nb_col):
                coord = (j, i)
                ajout_flag = ajouterFlagsGrilleDemineur(grille, coord)
                simplifier = simplifierGrilleDemineur(grille, coord)
                if not (coord in cell_deja_faite) and (len(ajout_flag) != 0 or len(simplifier) != 0) and isVisibleCellule(getCelluleGrilleDemineur(grille,coord)) == True :
                    cell_deja_faite.append(coord)
                    modif = 1
                    if len(ajout_flag) != 0:
                        coord_ajout_drapeau.append(ajout_flag)
                    if len(simplifier) != 0:
                        coord_rendue_visible.append(simplifier)
    return (set(coord_rendue_visible),set(coord_ajout_drapeau))