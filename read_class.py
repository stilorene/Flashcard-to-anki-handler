import tkinter as tk
from anki_import import get_anki_decks

def clear_frame(checkbox_frame):
     #Inhalt in Canvas, eher der frame (die Checkboxen) entfernen
    for widget in checkbox_frame.winfo_children():
        widget.destroy()


def get_selected_content(checkbox_save, checkbox_frame, selected_button, button_frame):
    selected_items = [text for var, text in checkbox_save if var.get()]
    print("Ausgewählt:", selected_items)

    clear_frame(checkbox_frame)
    
    print("Frameinhalt gelöscht")

    if not selected_items:
        tk.Label(checkbox_frame, 
            text="Keine Auswahl getroffen", 
            font=("Arial", 14, "bold"), 
            fg="#E74C3C",  # Ein schönes Rot für den Hinweis
            bg="lightgrey"
        ).pack(expand=True, fill=tk.BOTH, pady=50) # expand=True hilft beim Zentrieren
    else:
        # Ein Header, damit man weiß, was passiert
        tk.Label(
            checkbox_frame, 
            text="Gewählte Elemente:", 
            font=("Arial", 12, "underline"), 
            bg="lightgrey"
        ).pack(pady=(10, 20))

        for item in selected_items:
            tk.Label(
                checkbox_frame, 
                text=item, 
                font=("Arial", 12), 
                bg="white",       # Weißer Hintergrund für bessere Lesbarkeit
                padx=10, pady=5,  # Etwas "Luft" innerhalb des Labels
                relief="groove"   # Ein ganz leichter Rahmen (optional)
            ).pack(pady=10, padx=20, anchor="center")

    #Alter Button löschen, neuer erstellt
    selected_button.destroy()
    selected_button = tk.Button(button_frame, text="Auswahl akzeptieren", bg="#5B3CE7", fg="white", 
                   font=("Arial", 10, "bold"), padx=20, pady=8, command = lambda: which_stapel_import(checkbox_frame)) #wartet bis button geklick wurde.
    selected_button.pack(side=tk.LEFT, padx=10)  
    


def which_stapel_import(checkbox_frame):
    clear_frame(checkbox_frame)

    stapels = get_anki_decks()
    
    tk.Label(checkbox_frame, text="Gewählte Elemente:", font=("Arial", 12, "underline"), bg="lightgrey"
    ).pack(pady=(10, 20))


    #Stapel anzeigen lassen
    for item in stapels:
            tk.Label(
                checkbox_frame, 
                text=item, 
                font=("Arial", 12), 
                bg="white",       # Weißer Hintergrund für bessere Lesbarkeit
                padx=10, pady=5,  # Etwas "Luft" innerhalb des Labels
                relief="groove"   # Ein ganz leichter Rahmen (optional)
            ).pack(pady=10, padx=20, anchor="center")

    
  