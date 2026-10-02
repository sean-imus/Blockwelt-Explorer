# Meilenstein 7: Testklasse HouseTest
# Testet die Methode House.change_wall_material.
# Ausfuehren mit: uv run python -m unittest test_haus.py
# Hinweis: Beim Test oeffnet sich kurz ein Spiel-Fenster.
import unittest
from pyblockworld import World
from haus import House


class HouseTest(unittest.TestCase):

    def setUp(self):
        # Wird vor jedem Test ausgefuehrt: frische Welt und fertiges Haus erstellen
        self.welt = World()
        x, y, z = self.welt.player_position(as_int=True)
        # Haus auf Bodenhohe (y - 1) erstellen, damit es nicht schwebt
        self.haus = House((x + 2, y - 1, z + 3), self.welt)
        self.haus.build()

    def test_change_wall_material(self):
        # Nach dem Materialwechsel muessen alle vier Waende das neue Material haben.
        neues_material = "default:brick"
        self.haus.change_wall_material(neues_material)

        self.assertEqual(self.haus.wallFront.material_id, neues_material)
        self.assertEqual(self.haus.wallBack.material_id, neues_material)
        self.assertEqual(self.haus.wallLeft.material_id, neues_material)
        self.assertEqual(self.haus.wallRight.material_id, neues_material)


if __name__ == "__main__":
    unittest.main()
