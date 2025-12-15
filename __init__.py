from aqt import mw
from aqt.qt import *
from aqt.utils import tooltip
from aqt import gui_hooks


def link_selected_cards(browser):
    cids = browser.selectedCards()

    if not cids:
        tooltip("Keine Karten ausgewählt.")
        return

    # Festes Zielfeld
    target_field = "Link to Related Cards"
    source_field = "Word"  # Feld, aus dem das Wort genommen wird

    # Prüfen, ob das Quellfeld "Word" bei mindestens einer Karte existiert
    # (falls nicht, geben wir eine Warnung aus)
    try:
        first_card = mw.col.get_card(cids[0])
        note = first_card.note()
        if source_field not in note.keys():
            tooltip(f'Feld "{source_field}" existiert nicht in der Notizvorlage.')
            return
        if target_field not in note.keys():
            tooltip(f'Zielfeld "{target_field}" existiert nicht in der Notizvorlage.')
            return
    except Exception as e:
        tooltip(f"Fehler beim Zugriff auf die Karte: {e}")
        return

    # String mit "Word cidd..." für alle selektierten Karten zusammenbauen
    parts = []
    for cid in cids:
        try:
            card = mw.col.get_card(cid)
            note = card.note()
            word = note[source_field].strip() if note[source_field] else "(kein Wort)"
            parts.append(word)
            parts.append(f"cidd{cid}")
        except Exception:
            parts.append("(Fehler)")
            parts.append(f"cidd{cid}")

    new_content = " ".join(parts)

    mw.checkpoint("Link Cards")
    mw.progress.start()

    count = 0
    try:
        for cid in cids:
            card = mw.col.get_card(cid)
            note = card.note()

            # Alten Inhalt behalten und neuen anhängen
            # ÄNDERUNG: <br> einfügen für neue Zeile, wenn bereits Inhalt existiert
            current = note[target_field].strip()
            if current:
                note[target_field] = current + "<br>" + new_content
            else:
                note[target_field] = new_content

            mw.col.update_note(note)
            count += 1

    finally:
        mw.progress.finish()
        browser.model.reset()
        mw.reset()

    tooltip(f"Verknüpfungen in Feld '{target_field}' für {count} Karten angehängt.")


def setup_browser_menu(browser):
    action = QAction("Link Cards", browser)
    action.setShortcut(QKeySequence("Ctrl+Alt+L"))
    action.triggered.connect(lambda: link_selected_cards(browser))

    browser.form.menuEdit.addAction(action)


# Hook für neuere Anki-Versionen
gui_hooks.browser_menus_did_init.append(setup_browser_menu)