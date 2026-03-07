
import csv
import tkinter as tk
import prompt
from read_class import get_selected_content

#trennt den Text
def split_text(csv_text):
    lines = csv_text.strip().split('\n')
    return lines


def show_text():
    text = text_field.get("1.0", "end-1c")
    print("Eingegeben:\n", text)
    stripped_text = split_text(text)
    
    #Frame zerstören wenn nötig
    frame.destroy()
    print("Textfeld entfernt")
    
    # Canvas + Scrollbar für Checkboxen erstellen
    canvas = tk.Canvas(content_frame, highlightthickness=0, bg="lightgrey")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    scrollbar_vertical = tk.Scrollbar(content_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar_vertical.pack(side=tk.RIGHT, fill=tk.Y)
    
    scrollbar_horizontal = tk.Scrollbar(content_frame, orient=tk.HORIZONTAL, command=canvas.xview)
    scrollbar_horizontal.pack(side=tk.BOTTOM, fill=tk.X)
    
    canvas.configure(
        yscrollcommand=scrollbar_vertical.set,
        xscrollcommand=scrollbar_horizontal.set
    )
    
    # Frame INNERHALB des Canvas
    checkbox_frame = tk.Frame(canvas, bg="lightgrey")
    canvas.create_window((0, 0), window=checkbox_frame, anchor="nw")
    
    #Checkboxenelemente in einen Array Checkbox_save speichern
    checkbox_save = []
    
    for i in stripped_text:
        var = tk.BooleanVar()
        checkbox = tk.Checkbutton(
            checkbox_frame,
            text = i,
            anchor='w',
            variable=var,
            font=("Arial", 12),
            bg="lightgrey"
    )
        checkbox.pack(fill=tk.X, padx=5, pady=2)
        checkbox_save.append((var, i))
    #Aufruf der Funktion get_selected_content um ausgewählte Checkboxen zu zählen, und ausgeben
    selected = get_selected_content(checkbox_save)
    print(selected)
    
   # Mausrad-Support
    def on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
     # SHIFT + Mausrad = horizontal scrollen
    def on_shift_mousewheel(event):
        canvas.xview_scroll(int(-1*(event.delta/120)), "units")
    
    canvas.bind_all("<MouseWheel>", on_mousewheel)
    # SHIFT + Mausrad = horizontal scrollen
    canvas.bind_all("<Shift-MouseWheel>", on_shift_mousewheel)
    
    # Scrollregion aktualisieren
    checkbox_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))
    
import tkinter as tk

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(prompt.text)
    root.update()
    status_label.config(text="✓ Prompt wurde kopiert!", fg="green")
    root.after(2000, lambda: status_label.config(text="", fg="black"))
 

# Das UserInterface mit TkInter
root = tk.Tk()
root.title("Karteikarten Dashboard")
root.geometry("850x650")
root.config(bg="lightgrey")


# Textanzeige oben
label = tk.Label(root, text="Bitte Karteikarten hier einfügen", font=("Arial", 11), bg="lightgrey")
label.pack(pady=10)
#Checkboxen
content_frame = tk.Frame(root, bg="lightgrey")
content_frame.pack(pady=10, fill=tk.BOTH, expand=True)
# Textfeld mit Scrollbar
frame = tk.Frame(root, bg="lightgrey")
frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_field = tk.Text(frame, height=25, width=70, font=("Arial", 10), yscrollcommand=scrollbar.set)
text_field.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=text_field.yview)

# Button-Frame für bessere Anordnung
button_frame = tk.Frame(root, bg="lightgrey")
button_frame.pack(pady=10)

button = tk.Button(button_frame, text="Text ausgeben", bg="#E74C3C", fg="white", 
                   font=("Arial", 10, "bold"), padx=20, pady=8, command=show_text)
button.pack(side=tk.LEFT, padx=10)

copy_prompt = tk.Button(button_frame, text="Prompt für ChatGPT", bg="#27AE60", fg="white",
                        font=("Arial", 10, "bold"), padx=20, pady=8, command= copy_to_clipboard)
copy_prompt.pack(side=tk.LEFT, padx=10)

# Status-Label für Feedback
status_label = tk.Label(root, text="Prompt erfolgreich kopiert", bg="lightgrey", font=("Arial", 9))
status_label.pack(pady=5)

root.mainloop()