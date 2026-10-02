# Meilenstein 3: Beim Druecken von b werden zwei Waende in der Naehe des
# Spielers platziert - eine ungedreht und eine um 90 Grad um die Y-Achse gedreht.
# Starten mit: uv run python demo_3_waende.py
from pyblockworld import World
from wand import Wall


def b_gedrueckt(welt: World):
    # Position des Spielers holen (als ganze Zahlen)
    x, y, z = welt.player_position(as_int=True)

    # player_position() liegt beim Stehen auf dem Boden genau EINEN Block
    # ueber der Bodenoberflaeche - daher y - 1, damit die Waende nicht schweben.
    # Ungedrehte Wand: verläuft entlang der x-Achse
    wand_ungedreht = Wall((x + 2, y - 1, z + 2), welt)
    wand_ungedreht.build()

    # Gedrehte Wand: verläuft nach dem Drehen entlang der z-Achse
    wand_gedreht = Wall((x + 10, y - 1, z + 2), welt)
    wand_gedreht.rotated = True           # rotated=True = um 90 Grad um die Y-Achse gedreht
    wand_gedreht.build()


# Neue Welt erstellen und die Funktion fuer die Bauen-Taste (b) zuweisen
welt = World()
welt.build_key_pressed = b_gedrueckt
# Welt starten
welt.run()
