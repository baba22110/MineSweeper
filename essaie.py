from Model.GrilleDemineur import *
from Model.Cellule import *

grille=construireGrilleDemineur(4,5)
print(grille)
print(getCoordonneeVoisinsGrilleDemineur(grille,(0,0)))
