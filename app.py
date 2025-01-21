import tkinter as tk
import random

from util_function.generate_meta import generate_meta_discription, result_anzeigen
# Erstellen des Hauptfensters
root = tk.Tk()
root.title("Meta-Generator")
root.geometry("350x500")
# Fenstergröße nicht veränderbar machen
root.resizable(False, False)



label = tk.Label(root, text="Meta Description Generieren", font=("Arial", 14))
label.config()
label.grid(row=0, column=0, columnspan=2,  padx=10, pady=10, sticky="nsew") 

# Erstellen und Platzieren der Labels und Eingabefelder
titel_label = tk.Label(root, text="Titel:")
titel_label.grid(row=1, column=0, padx=10, pady=5)
titel_entry = tk.Entry(root, width=20)
titel_entry.grid(row=1, column=1, padx=10, pady=5)

vorname_label = tk.Label(root, text="Vorname:")
vorname_label.grid(row=2, column=0, padx=10, pady=5)
vorname_entry = tk.Entry(root)
vorname_entry.grid(row=2, column=1, padx=10, pady=5)

nachname_label = tk.Label(root, text="Nachname:")
nachname_label.grid(row=3, column=0, padx=10, pady=5)
nachname_entry = tk.Entry(root)
nachname_entry.grid(row=3, column=1, padx=10, pady=5)

def generate_meta():
    result_de, result_en = generate_meta_discription(titel_entry, vorname_entry, nachname_entry)
    if result_de != "" and result_en != "":
        result_anzeigen(result_text_area_de, result_text_area_en, result_de, result_en)

# Button zur Generierung des zufälligen Textes
generate_button = tk.Button(root, text="Meta Description Generieren", command=generate_meta)
generate_button.grid(row=4, column=0, columnspan=2, pady=20)

# Textarea zur Anzeige der beiden generierten Texte
de_label = tk.Label(root, text="Meta auf Deutsch:", font=("Arial", 12))
de_label.grid(row=5, column=0)
result_text_area_de = tk.Text(root, height=6, width=40)
result_text_area_de.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

en_label = tk.Label(root, text="Meta auf Englisch:", font=("Arial", 12))
en_label.grid(row=7, column=0)
result_text_area_en = tk.Text(root, height=6, width=40)
result_text_area_en.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

# Starten der Anwendung
root.mainloop()
