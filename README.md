# Link Cards Anki Add-on

Dieses Add-on fügt dem Anki Browser eine Funktion hinzu, um ausgewählte Karten miteinander zu verlinken. Es dient dazu, Beziehungen zwischen verschiedenen Vokabelkarten (z.B. ähnliche Wörter, Synonyme, Antonyme) im Feld `"Link to Related Cards"` zu speichern.

## Wichtiger Hinweis zur Kompatibilität

**Dieses Add-on funktioniert nur, wenn alle folgenden Bedingungen erfüllt sind:**

1. **Notiztyp:** Der verwendete Notiztyp muss die Felder **`Word`** (als Quelle des verlinkten Begriffs) und **`Link to Related Cards`** (als Zielfeld für die Verlinkung) enthalten.
2. **Abhängiges Add-on:** Zur **Anzeige** der erzeugten Links auf der Karte musst du das Add-on **"Hyperlink Note IDs"** installieren.
    * **AnkiWeb Code:** **1423933177**

Dieses Add-on wurde speziell für Notiztypen wie **"MiningSimple"** entwickelt und getestet.

## Installation
Lade den Ordner herunter und verschiebe ihn in deinen Anki Add-ons Ordner.

## Nutzung
1. Öffne den Anki **Browser** (`B`).
2. Markiere alle Karten, die du miteinander verlinken möchtest (z.B. 2-3 verwandte Vokabeln).
3. Gehe im Menü auf **"Bearbeiten" (Edit)** -> **"Link Cards"**.
4. Alternativ nutze den Shortcut **`Strg` + `Alt` + `L`** (Windows/Linux) oder **`Cmd` + `Alt` + `L`** (Mac).

Die **Wörter** und **Karten-IDs** aller ausgewählten Karten werden nun im Feld `"Link to Related Cards"` jeder dieser Notizen hinzugefügt, wobei jede neue Verlinkung in einer neuen Zeile beginnt.
