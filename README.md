# Blockwelt-Explorer (ITF25)

Schulprojekt LF8: Eine Erweiterung für ein an Minecraft angelehntes Spiel.
Mit der Erweiterung können Gebäude modular **auf Knopfdruck (Taste `b`)** in der Welt gebaut werden.

Die Bibliothek `pyblockworld` wird benutzt (Installation siehe unten). Alle Standardwerte für Maße
und Materialien stammen aus dem Klassendiagramm der Testatkarte.

## Installation und Start

```bash
uv sync                 # Abhängigkeiten (pyblockworld) installieren
uv run python main.py   # Spiel starten
```

Im Spiel mit der Maus umsehen, laufen (WASD) und mit **Leertaste** springen.
Drückt man **`b`**, wird das Haus in der Nähe des Spielers gebaut.

Zum Ausführen der einzelnen Meilensteine:

```bash
uv run python demo_1_erste_bloecke.py        # MS 1: unterschiedliche Blöcke auf Knopfdruck
uv run python demo_2_blockkoerper.py         # MS 2: 3 Blöcke in x-, 4 in y-, 5 in z-Richtung
uv run python demo_3_waende.py               # MS 3: zwei Wände (eine gedreht, eine ungedreht)
uv run python demo_4_fenster_und_tuer.py     # MS 4: vier Wände (von jedem Typ eine gedreht)
uv run python main.py                        # MS 7: komplettes Haus
uv run python -m unittest test_haus.py       # MS 7: Testklasse HouseTest
```

## Aufbau des Projekts

| Datei | Inhalt |
|---|---|
| `demo_1_erste_bloecke.py` | Meilenstein 1: unterschiedliche Blöcke auf Knopfdruck |
| `demo_2_blockkoerper.py` | Meilenstein 2: Blockkörper 3×4×5 mit verschiedenen Materialien |
| `class_wall.py` | Klasse `Wall` (Meilenstein 3) |
| `demo_3_waende.py` | Meilenstein 3: zwei Wände, eine gedreht |
| `class_wall_with_window.py` | Klasse `WallWithWindow` (Meilenstein 4) |
| `class_wall_with_door.py` | Klasse `WallWithDoor` (Meilenstein 4) |
| `demo_4_fenster_und_tuer.py` | Meilenstein 4: vier Wände |
| `class_roof.py` | Klasse `Roof` (Meilenstein 6) |
| `class_house.py` | Klasse `House` (Meilenstein 7) |
| `main.py` | Fertiges Programm: Haus auf Knopfdruck |
| `test_haus.py` | Klasse `HouseTest` mit `test_change_wall_material` |

## Erläuterungen aus der Testatkarte

### Bedeutung des Pfeiles zur Klasse `Wall` (Meilenstein 4)

Der Pfeil mit der offenen (leeren) Pfeilspitze von `WallWithWindow` und `WallWithDoor` zur Klasse
`Wall` bedeutet **Vererbung** („ist ein“-Beziehung): Eine Wand mit Fenster **ist eine** Wand.
`WallWithWindow` und `WallWithDoor` erben alle Attribute und Methoden von `Wall`
(`pos`, `width`, `height`, `rotated`, `material_id`, `build()`), ergänzen je ein eigenes Attribut
(`window_material_id` bzw. `door_material_id`) und überschreiben `build()`, um zusätzlich das
Fenster bzw. die Tür auszuschneiden. In Python steht das Schlüsselwort `super().__init__(...)`
für den Aufruf des Konstruktors der Basisklasse.

### Bedeutung der Raute (Meilenstein 6)

Die Raute sitzt in der Beziehung zwischen `Roof` (bzw. `Wall`) und `House` **am Ganzen**, also an
der Klasse `House`. Sie bedeutet **Aggregation/Komposition**:

- **Aggregation**: Ein Ganzes besteht aus Teilen, die auch ohne das Ganze existieren können
  (ungefüllte Raute).
- **Komposition**: Ein Ganzes besteht aus Teilen, die ohne das Ganze nicht sinnvoll existieren
  (gefüllte Raute). Das Ganze erzeugt und besitzt seine Teile.

Im Klassendiagramm ist die Raute **gefüllt** → **Komposition**: Das `House` erzeugt seine Wände und
sein Dach selbst (im Konstruktor) und besitzt sie. Ein einzelnes Dach, das neben einem Haus in der
Welt liegt, ist kein sinnvolles Objekt des Hauses mehr.

### Unterschiede zwischen public, private und protected (Meilenstein 5)

Die Vorzeichen im Klassendiagramm geben die **Sichtbarkeit** an:

| Sichtbarkeit | Zeichen | Bedeutung | In Python |
|---|---|---|---|
| **public** | `+` | Von überall erreichbar (eigene Klasse, Unterklassen, Fremder Code) | normaler Name, z. B. `self.pos` |
| **protected** | `#` | Nur innerhalb der eigenen Klasse und ihrer Unterklassen sichtbar | Konvention: ein Unterstrich, z. B. `self._bw` |
| **private** | `-` | Nur innerhalb der eigenen Klasse sichtbar, nicht in Unterklassen und nicht von außen | Konvention: zwei Unterstriche, z. B. `self.__bw` („Name Mangling“) |

Python erzwingt Sichtbarkeit nicht wirklich (alles ist technisch öffentlich), aber die
Konventionen `_name` und `__name` zeigen anderen Entwicklern: „Nicht von außen benutzen!“
Bei `__name` benennt Python das Attribut zusätzlich um (`_Klassenname__name`), damit es nicht
versehentlich von außen oder in Unterklassen überschrieben wird.

Im Projekt wurde das umgesetzt wie im Diagramm:

- `Wall._bw` → **protected**, weil die Unterklassen `WallWithWindow` und `WallWithDoor` darauf zugreifen dürfen.
- `Roof.__bw` und `House.__bw` → **private**, nur die eigene Klasse benutzt sie.
- alle übrigen Attribute und Methoden (z. B. `pos`, `width`, `build()`, `change_wall_material()`) → **public**.

## Tests

```bash
uv run python -m unittest test_haus.py
```

`HouseTest.setUp()` erstellt eine Welt und ein fertiges Haus,
`test_change_wall_material()` prüft, ob nach dem Aufruf von `House.change_wall_material()`
alle vier Wände das neue Material haben.
