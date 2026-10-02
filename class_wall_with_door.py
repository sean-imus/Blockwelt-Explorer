# Meilenstein 4: Wand mit Türausschnitt
# Erbt ebenfalls von Wall (Vererbung).
from pyblockworld import World
from class_wall import Wall


class WallWithDoor(Wall):

    def __init__(self, pos: tuple, bw: World):
        super().__init__(pos, bw)
        self.door_material_id = "air"        # "air" schneidet ein Loch = Tuer

    def build(self):
        # Erst die massive Erben-Wand bauen, dann die Tuer ausschneiden.
        super().build()
        # Tuer: 2 Bloecke breit, 3 Bloecke hoch, direkt ab Boden (damit man durchlaufen kann).
        start = (self.width - 2) // 2
        for dx in range(start, start + 2):
            for dy in range(0, 3):
                bx, by, bz = self._block_position(dx, dy)
                self._bw.setBlock(bx, by, bz, self.door_material_id)
