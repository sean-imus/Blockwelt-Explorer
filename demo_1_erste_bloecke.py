# Meilenstein 1: Auf Knopfdruck erscheinen unterschiedliche Bloecke
# in der Naehe des Spielers.
# Starten mit: uv run python demo_1_erste_bloecke.py
# Dann im Spiel die B-Taste druecken.
from pyblockworld import World


# Diese Funktion wird aufgerufen, sobald die B-Taste (Bauen-Taste) gedrueckt wird.
def b_gedrueckt(welt: World):
    # Position des Spielers holen (als ganze Zahlen)
    x, y, z = welt.player_position(as_int=True)

    # Vier unterschiedliche Bloecke nebeneinander vor dem Spieler platzieren
    welt.setBlock(x + 2, y, z + 2, "default:brick")   # Ziegel
    welt.setBlock(x + 3, y, z + 2, "default:stone")   # Stein
    welt.setBlock(x + 4, y, z + 2, "default:sand")    # Sand
    welt.setBlock(x + 5, y, z + 2, "default:grass")   # Gras


# Neue Welt erstellen und die Funktion fuer die Bauen-Taste (b) zuweisen
welt = World()
welt.build_key_pressed = b_gedrueckt
# Welt starten
welt.run()
