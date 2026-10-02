# Meilenstein 3: Klasse Wall nach dem Klassendiagramm
# Eine Wand ist width Bloecke breit, height Bloecke hoch und steht auf der
# Unterseite am Punkt pos (untere linke Ecke).
from pyblockworld import World


class Wall:

    def __init__(self, pos: tuple, bw: World):
        self.pos = pos
        self.width = 6                       # Standardwerte aus dem Klassendiagramm
        self.height = 5
        self.rotated = False                 # False = ungedreht, True = um 90 Grad um die Y-Achse gedreht
        self.material_id = "default:stone"
        self._bw = bw                        # protected (siehe Klassendiagramm '#'): nur fuer die Klasse und Unterklassen

    def build(self):
        # Baut die Wand aus einem Blockbereich: width Blöcke lang, height Blöcke hoch, 1 Block dick.
        # Ungedreht verläuft die Wand entlang der x-Achse, gedreht entlang der z-Achse.
        x, y, z = self.pos
        if self.rotated:
            self._bw.setBlocks(x, y, z, x, y + self.height - 1, z + self.width - 1, self.material_id)
        else:
            self._bw.setBlocks(x, y, z, x + self.width - 1, y + self.height - 1, z, self.material_id)

    def _block_position(self, dx: int, dy: int) -> tuple:
        # protected Hilfsmethode: rechnet einen Versatz (dx = entlang der Wand, dy = Hoehe)
        # in die passenden Weltkoordinaten um. Dadurch funktionieren Fenster und Tuer
        # bei gedrehten und ungedrehten Waenden.
        x, y, z = self.pos
        if self.rotated:
            return x, y + dy, z + dx
        return x + dx, y + dy, z
