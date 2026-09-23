import tkinter as tk
from anki_import import create_anki_deck, get_anki_decks

# Hält den aktuell ausgewählten Deck-Namen
SELECTED_DECK = ""  # Wird später als tk.StringVar() initialisiert

def clear_frame(checkbox_frame):
    # Inhalt in Canvas, eher der frame (die Checkboxen) entfernen
    for widget in checkbox_frame.winfo_children():
        widget.destroy()


def get_selected_content(checkbox_save, checkbox_frame, selected_button, button_frame):
    selected_items = [text for var, text in checkbox_save if var.get()]
    print("Ausgewählt:", selected_items)

    clear_frame(checkbox_frame)

    print("Frameinhalt gelöscht")

    if not selected_items:
        tk.Label(
            checkbox_frame,
            text="Keine Auswahl getroffen",
            font=("Arial", 14, "bold"),
            fg="#E74C3C",
            bg="lightgrey",
        ).pack(expand=True, fill=tk.BOTH, pady=50)
    else:
        tk.Label(
            checkbox_frame,
            text="Gewählte Elemente:",
            font=("Arial", 12, "underline"),
            bg="lightgrey",
        ).pack(pady=(10, 20))

        for item in selected_items:
            tk.Label(
                checkbox_frame,
                text=item,
                font=("Arial", 12),
                bg="white",
                padx=10,
                pady=5,
                relief="groove",
            ).pack(pady=10, padx=20, anchor="center")

    # Alter Button löschen, neuer erstellt
    selected_button.destroy()
    selected_button = tk.Button(
        button_frame,
        text="Auswahl akzeptieren",
        bg="#5B3CE7",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=20,
        pady=8,
        command=lambda: which_stapel_import(checkbox_frame, button_frame, selected_button),
    )
    selected_button.pack(side=tk.LEFT, padx=10)


def show_create_deck_dialog(checkbox_frame):
    root_window = checkbox_frame.winfo_toplevel()
    dialog = tk.Toplevel(root_window)
    dialog.title("Neuen Stapel anlegen")
    dialog.geometry("420x180")
    dialog.transient(root_window)
    dialog.grab_set()
    dialog.config(bg="lightgrey")

    tk.Label(
        dialog,
        text="Bitte gib den Namen des neuen Stapels ein:",
        font=("Arial", 11, "bold"),
        bg="lightgrey",
    ).pack(anchor="w", padx=20, pady=(20, 10))

    entry_var = tk.StringVar()
    entry = tk.Entry(dialog, textvariable=entry_var, width=40, font=("Arial", 11))
    entry.pack(padx=20, fill=tk.X)

    status_label = tk.Label(
        dialog,
        text="",
        fg="#E74C3C",
        bg="lightgrey",
        font=("Arial", 10),
        wraplength=360,
        justify="left",
    )
    status_label.pack(anchor="w", padx=20, pady=(8, 0))

    def submit_new_deck():
        deck_name = entry_var.get().strip()

        if not deck_name:
            status_label.config(text="Bitte gib einen Namen für den neuen Stapel ein.")
            entry.focus_set()
            return

        if create_anki_deck(deck_name):
            dialog.destroy()
            which_stapel_import(checkbox_frame)
            return

        status_label.config(
            text="Der Stapel konnte nicht angelegt werden. Prüfe die Anki-Verbindung und den Namen."
        )

    button_row = tk.Frame(dialog, bg="lightgrey")
    button_row.pack(pady=20)

    tk.Button(
        button_row,
        text="Anlegen",
        bg="#27AE60",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=20,
        pady=8,
        command=submit_new_deck,
    ).pack(side=tk.LEFT, padx=10)

    tk.Button(
        button_row,
        text="Abbrechen",
        bg="#E74C3C",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=20,
        pady=8,
        command=dialog.destroy,
    ).pack(side=tk.LEFT, padx=10)

    entry.focus_set()
    entry.bind("<Return>", lambda event: submit_new_deck())


def which_stapel_import(checkbox_frame, button_frame, selected_button):
    clear_frame(checkbox_frame)

    stapels = get_anki_decks()

    tk.Label(
        checkbox_frame,
        text="Stapel auswählen:",
        font=("Arial", 12, "underline"),
        bg="lightgrey",
    ).pack(pady=(10, 10))

    tk.Button(
        checkbox_frame,
        text="Neuen Stapel anlegen",
        bg="#27AE60",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=20,
        pady=8,
        command=lambda: show_create_deck_dialog(checkbox_frame),
    ).pack(pady=(0, 15))

    if not stapels:
        tk.Label(
            checkbox_frame,
            text="Keine Stapel gefunden. Bitte stelle sicher, dass Anki läuft und AnkiConnect aktiv ist.",
            font=("Arial", 11),
            bg="lightgrey",
            fg="#E74C3C",
        ).pack(pady=20)
        return

    #Alter Button (Auswahl akzeptieren) löschen, neuer Button wird erstellt;
    selected_button.destroy()
    selected_button = tk.Button(
        button_frame,
        text="In ausgewählten Stapel importieren",
        bg="#5B3CE7",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=20,
        pady=8,
        command=lambda: (checkbox_frame),
        # #Funktionsaufruf hier anpassen, um den ausgewählten Stapel zu verwenden;
    )
    selected_button.pack(side=tk.LEFT, padx=10)

    selected_deck_button = None

    # Funktion, um den ausgewählten Stapel zu speichern und die Button-Farbe zu ändern
    def handle_deck_click(current_item, current_button):
        nonlocal selected_deck_button
        global SELECTED_DECK  # Zugriff auf die globale Variable

        if (
            selected_deck_button is not None
            and selected_deck_button is not current_button
        ):
            selected_deck_button.config(bg="white", fg="black", relief="raised")

        current_button.config(bg="#27AE60", fg="white", relief="sunken")
        selected_deck_button = current_button
        # print(f"Stapel ausgewählt: {current_item}")
        SELECTED_DECK = current_item
        print(f"SELECTED_DECK aktualisiert: {SELECTED_DECK}");

    for item in stapels:
        if item == "Standard":
            continue
        if item == "Default":
            continue

        deck_button = tk.Button(
            checkbox_frame,
            text=item,
            font=("Arial", 12),
            bg="white",
            padx=10,
            pady=6,
            relief="raised",
        )
        deck_button.config(
            command=lambda item=item, deck_button=deck_button: handle_deck_click(
                item, deck_button
            )
        )
        deck_button.pack(pady=8, padx=20, anchor="center", fill=tk.X)

    checkbox_frame.update_idletasks()
