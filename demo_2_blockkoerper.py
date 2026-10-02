# Meilenstein 2: Kommentiertes Programm, das 3 Bloecke in x-Richtung,
# 4 Bloecke in y-Richtung und 5 Bloecke in z-Richtung platziert.
# Es werden unterschiedliche Materialien verwendet und der Blockkoerper
# steht in der Naehe des Spielers.
# Starten mit: uv run python demo_2_blockkoerper.py
# Dann im Spiel die B-Taste druecken.
from pyblockworld import World


def b_gedrueckt(welt: World):
    # Position des Spielers holen (als ganze Zahlen)
    x, y, z = welt.player_position(as_int=True)

    # Der Koerper soll 3 Bloecke in x, 4 Bloecke in y und 5 Bloecke in z gross sein.
    # Deshalb: x bleibt x+2 bis x+4 (3 Bloecke), y von y bis y+3 (4 Bloecke),
    # z von z+2 bis z+6 (5 Bloecke).
    x1, y1, z1 = x + 2, y, z + 2          # vordere untere Ecke
    x2, y2, z2 = x + 4, y + 3, z + 6      # hintere obere Ecke

    # Unterer Teil (2 Bloecke hoch) aus Stein
    welt.setBlocks(x1, y1, z1, x2, y1 + 1, z2, "default:stone")
    # Mittlerer Teil (1 Block hoch) aus Sand
    welt.setBlocks(x1, y1 + 2, z1, x2, y1 + 2, z2, "default:sand")
    # Oberer Teil (1 Block hoch) aus Ziegeln
    welt.setBlocks(x1, y1 + 3, z1, x2, y1 + 3, z2, "default:brick")


# Neue Welt erstellen und die Funktion fuer die Bauen-Taste (b) zuweisen
welt = World()
welt.build_key_pressed = b_gedrueckt
# Welt starten
welt.run()
