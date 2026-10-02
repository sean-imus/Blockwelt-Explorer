# Meilenstein 5+7: Klasse House nach dem Klassendiagramm
# Ein Haus besteht aus einer Wand mit Tuer (vorn), zwei Waenden mit Fenstern
# (links und rechts), einer massiven Wand (hinten) und einem Dach.
# Sichtbarkeiten wie im Klassendiagramm: Waende/Dach/pos public, bw private.
from pyblockworld import World
from class_wall import Wall
from class_wall_with_window import WallWithWindow
from class_wall_with_door import WallWithDoor
from class_roof import Roof


class House:

    def __init__(self, pos: tuple, bw: World):
        self.pos = pos
        self.__bw = bw                       # private (siehe Klassendiagramm '-')
        x, y, z = pos

        # Vordere Wand mit Tuer, ungedreht (verläuft entlang der x-Achse)
        self.wallFront = WallWithDoor((x, y, z), bw)
        # Masse von der fertigen Wand uebernehmen (Breite 6 = Grundflaeche 6x6, Hoehe 5)
        laenge = self.wallFront.width
        hoehe = self.wallFront.height

        # Hintere Wand: massiv, gegenueber der Vorderwand
        self.wallBack = Wall((x, y, z + laenge - 1), bw)

        # Linke Wand mit Fenster, gedreht (verläuft entlang der z-Achse)
        self.wallLeft = WallWithWindow((x, y, z), bw)
        self.wallLeft.rotated = True

        # Rechte Wand mit Fenster, gedreht, an der rechten Grundflaeche
        self.wallRight = WallWithWindow((x + laenge - 1, y, z), bw)
        self.wallRight.rotated = True

        # Dach liegt oben auf den Waenden
        self.roof = Roof((x, y + hoehe, z), bw)

    def build(self):
        # Baut das ganze Haus: alle vier Waende und das Dach.
        self.wallFront.build()
        self.wallBack.build()
        self.wallLeft.build()
        self.wallRight.build()
        self.roof.build()

    def change_wall_material(self, new_material_id: str):
        # Setzt fuer alle vier Waende ein neues Material und baut das Haus neu.
        self.wallFront.material_id = new_material_id
        self.wallBack.material_id = new_material_id
        self.wallLeft.material_id = new_material_id
        self.wallRight.material_id = new_material_id
        self.build()
