# Meilenstein 4: Wand mit Fensterausschnitt
# Erbt von Wall (Pfeil im Klassendiagramm = Vererbung: "ist eine" Wall).
from pyblockworld import World
from class_wall import Wall


class WallWithWindow(Wall):

    def __init__(self, pos: tuple, bw: World):
        super().__init__(pos, bw)
        self.window_material_id = "air"      # "air" schneidet ein Loch = Fenster

    def build(self):
        # Erst die massive Erben-Wand bauen, dann das Fenster ausschneiden.
        super().build()
        # Fenster: 2 Bloecke breit, 2 Bloecke hoch, mittig ueber Bodenhoehe.
        start = (self.width - 2) // 2
        for dx in range(start, start + 2):
            for dy in range(2, 4):
                bx, by, bz = self._block_position(dx, dy)
                self._bw.setBlock(bx, by, bz, self.window_material_id)
