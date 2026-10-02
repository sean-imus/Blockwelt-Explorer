# Meilenstein 7 (letztes Programm): Beim Druecken von b wird ein komplettes
# Haus in der Naehe des Spielers errichtet (Wand mit Tuer, zwei Waende mit
# Fenstern, eine massive Wand und ein Dach).
# Starten mit: uv run python main.py
from pyblockworld import World
from class_house import House


def b_gedrueckt(welt: World):
    # Position des Spielers holen (als ganze Zahlen)
    x, y, z = welt.player_position(as_int=True)

    # Haus mit etwas Abstand zum Spieler bauen (Spieler steht dann vor der Tuer).
    # player_position() liegt beim Stehen auf dem Boden genau EINEN Block
    # ueber der Bodenoberflaeche - daher y - 1, damit das Haus nicht schwebt.
    haus = House((x + 2, y - 1, z + 3), welt)
    haus.build()


# Neue Welt erstellen und die Funktion fuer die Bauen-Taste (b) zuweisen
welt = World()
welt.build_key_pressed = b_gedrueckt
# Welt starten
welt.run()
