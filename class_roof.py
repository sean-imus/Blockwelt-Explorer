# Meilenstein 6: Klasse Roof nach dem Klassendiagramm
# Das Dach ist eine flache Platte: width x depth Bloecke, 1 Block dick,
# auf der Unterseite am Punkt pos.
# Die Raute im Klassendiagramm zeigt zu House: Aggregation/Komposition (siehe README).
from pyblockworld import World


class Roof:

    def __init__(self, pos: tuple, bw: World):
        self.pos = pos
        self.width = 6                       # Standardwerte aus dem Klassendiagramm
        self.depth = 6
        self.roof_material_id = "default:brick"
        self.__bw = bw                       # private (siehe Klassendiagramm '-'): nur innerhalb der Klasse

    def build(self):
        # Baut die Dachplatte: width Blöcke entlang x, depth Blöcke entlang z, auf einer Hoehe.
        x, y, z = self.pos
        self.__bw.setBlocks(x, y, z, x + self.width - 1, y, z + self.depth - 1, self.roof_material_id)
