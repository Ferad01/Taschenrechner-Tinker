import tkinter as tk

# Hauptfenster
root = tk.Tk()
root.title("Taschenrechner")
root.geometry("350x500")
root.configure(bg="white")

# Eingabefeld
entry = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="sunken", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

# Funktionen
def button_click(symbol):
    entry.insert(tk.END, symbol)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Fehler")

# Buttons definieren
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Buttons erzeugen
for row_index, row in enumerate(buttons):
    for col_index, symbol in enumerate(row):
        if symbol == '=':
            command = calculate
        else:
            command = lambda s=symbol: button_click(s)
        
        btn = tk.Button(root, text=symbol, font=("Arial", 18), width=5, height=2,
                        bg="#f0f0f0", relief="raised", command=command)
        btn.grid(row=row_index + 1, column=col_index, padx=10, pady=10, sticky="nsew")

# Clear-Button unten
clear_btn = tk.Button(root, text="C", font=("Arial", 18), width=5, height=2,
                      bg="#ffcccc", relief="raised", command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

# Dynamisches Layout (Fenster skalierbar machen)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# App starten
root.mainloop()
