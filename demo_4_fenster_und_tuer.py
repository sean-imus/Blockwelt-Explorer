# Meilenstein 4: Beim Druecken von b werden zwei Waende von jedem Typ in der
# Naehe des Spielers platziert - jeweils eine gedreht und eine ungedreht.
# Insgesamt also vier Waende (2x mit Fenster, 2x mit Tuer).
# Starten mit: uv run python demo_4_fenster_und_tuer.py
from pyblockworld import World
from wand_mit_fenster import WallWithWindow
from wand_mit_tuer import WallWithDoor


def b_gedrueckt(welt: World):
    # Position des Spielers holen (als ganze Zahlen)
    x, y, z = welt.player_position(as_int=True)

    # player_position() liegt beim Stehen auf dem Boden genau EINEN Block
    # ueber der Bodenoberflaeche - daher y - 1, damit die Waende nicht schweben.

    # Wand mit Fenster, ungedreht
    fenster_1 = WallWithWindow((x + 2, y - 1, z + 2), welt)
    fenster_1.build()

    # Wand mit Fenster, gedreht
    fenster_2 = WallWithWindow((x + 10, y - 1, z + 2), welt)
    fenster_2.rotated = True
    fenster_2.build()

    # Wand mit Tuer, ungedreht
    tuer_1 = WallWithDoor((x + 2, y - 1, z + 9), welt)
    tuer_1.build()

    # Wand mit Tuer, gedreht
    tuer_2 = WallWithDoor((x + 10, y - 1, z + 9), welt)
    tuer_2.rotated = True
    tuer_2.build()


# Neue Welt erstellen und die Funktion fuer die Bauen-Taste (b) zuweisen
welt = World()
welt.build_key_pressed = b_gedrueckt
# Welt starten
welt.run()
