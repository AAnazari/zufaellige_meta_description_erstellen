import random
import tkinter as tk
from tkinter import messagebox

from data.text_list import list_text_auf_deutsch, list_text_auf_englisch
def generate_meta_discription(titel_entry, vorname_entry, nachname_entry):

    result_text_auf_de = ""
    result_text_auf_en = ""

    titel = titel_entry.get().strip()
    vorname = vorname_entry.get().strip()
    nachname = nachname_entry.get().strip()
    
    if titel == "":
        messagebox.showerror("Titel", "Bitte gebe einen Titel ein.")
    elif vorname == "":
        messagebox.showerror("Vorname", "Bitte gebe einen Vornamen ein.")
    elif nachname == "":
        messagebox.showerror("Nachname", "Bitte gebe einen Nachnamen ein.")
    else:
        # Wählen Sie einen zufälligen Index
        random_index_a = random.randint(0, len(list_text_auf_deutsch) - 1)

        # Titel Entry leeren
        entry_leeren(titel_entry)
        # Vorname Entry leeren
        entry_leeren(vorname_entry)
        # Nachname Entry leeren
        entry_leeren(nachname_entry)


        
        # Verwenden Sie denselben Index, um aus andere Liste auszuwählen
        result_text_auf_de = list_text_auf_deutsch[random_index_a].format(titel, vorname, nachname)
        result_text_auf_en = list_text_auf_englisch[random_index_a].format(titel, vorname, nachname)
        
    return result_text_auf_de, result_text_auf_en

def result_anzeigen(area_de, area_en, result_de, result_en):
    # Aktualisieren
    area_de.delete(1.0, tk.END)
    area_de.insert(tk.END, result_de)
    area_en.delete(1.0, tk.END)
    area_en.insert(tk.END, result_en)

def entry_leeren(entry):
    entry.delete(0, tk.END)
