def get_selected_content(checkbox_save):
    selected_items = [text for var, text in checkbox_save if var.get()]
    print("Ausgewählt:", selected_items)
    return selected_items