from Controller.Controller import Controller
from View.MineSweeper import MineSweeper
from Model.Cellule import *
from Model.Constantes import *
const.MA_PREMIERE_CONSTANTE = "Ceci est une constante chaîne de caractères"
const.MA_SECONDE_CONSTANTE = 3.14




# Essais graphiques
#

# Calcul de la taille de la fenêtre
# Nombre de cellules
CELL_LINE_COUNT = 16
CELL_COLUMN_COUNT = 16

controller = Controller(CELL_LINE_COUNT, CELL_COLUMN_COUNT)
mines = MineSweeper(controller, CELL_LINE_COUNT, CELL_COLUMN_COUNT)
controller.set_win(mines)

mines.play()
