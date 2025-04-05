🧮 Taschenrechner mit Python & Tkinter
Ein einfacher grafischer Taschenrechner mit grundlegenden Rechenfunktionen, erstellt mit Python und der tkinter-Bibliothek.

📸 Vorschau
(Hier kannst du einen Screenshot der App einfügen)

🚀 Features
Schlichtes, modernes UI

Grundrechenarten: +, -, *, /

Dezimalzahlen möglich (.)

Dynamisch skalierbares Layout (auch bei Fenstervergrößerung)

Fehlerbehandlung bei ungültigen Eingaben

"C"-Button zum Zurücksetzen

🛠️ Technologien
Python 3

tkinter (Standard-GUI-Bibliothek in Python)

📦 Installation & Ausführung
Python installieren (falls noch nicht geschehen):
👉 https://www.python.org/downloads/

Datei ausführen:

bash
Kopieren
Bearbeiten
python taschenrechner.py
🧠 Codeüberblick
button_click(symbol): Fügt das Symbol ins Eingabefeld ein

clear(): Löscht das Eingabefeld

calculate(): Führt die Berechnung durch (mit eval()) und zeigt das Ergebnis oder "Fehler" bei ungültigem Ausdruck

⚠️ Hinweis
Dieser Taschenrechner nutzt eval() zur Berechnung. In einer realen Anwendung ist das potenziell unsicher – besonders wenn Eingaben von Nutzer:innen verarbeitet werden, die du nicht kontrollierst.
