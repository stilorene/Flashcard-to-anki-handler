# AI Coding Guidelines for Flashcard CSV Manager

## Project Overview
This is a Tkinter-based GUI application for managing flashcards stored in CSV format. The app allows users to paste CSV text, select flashcards via checkboxes, and copy ChatGPT prompts to clipboard.

## Architecture
- **main.py**: Core GUI application with Tkinter interface, text input handling, checkbox generation, and clipboard operations
- **prompt.py**: Contains hardcoded flashcard data as a multi-line string in German
- **read_class.py**: Utility module with `get_selected_content()` function for processing checkbox selections

## Key Patterns & Conventions

### Flashcard Format
Store flashcards as semicolon-separated Q&A pairs:
```
Question?;Answer.
Another question?;Corresponding answer.
```

### GUI Styling
Use consistent lightgrey theme throughout:
- Background: `bg="lightgrey"`
- Font: `font=("Arial", 12)` for checkboxes, `font=("Arial", 10)` for text fields
- Button styling: Red for primary actions (`bg="#E74C3C"`), green for secondary (`bg="#27AE60"`)

### Code Structure
- Use German for comments, variable names, and UI text
- Keep functions simple and focused (single responsibility)
- Global variables for Tkinter widgets (root, frames, etc.)
- Import structure: standard library first, then local modules

### Checkbox Implementation
Follow the pattern in `main.py` lines 25-45:
- Create canvas with scrollbars for large lists
- Store checkboxes in array: `checkbox_save = []`
- Each item: `(BooleanVar(), text)`
- Bind mousewheel events for scrolling

### Clipboard Operations
Use Tkinter's clipboard API:
```python
root.clipboard_clear()
root.clipboard_append(text)
root.update()
```

## Development Workflow
- Run directly: `python main.py`
- No build system or dependencies required
- GUI testing requires manual interaction
- Debug with print statements (as seen throughout codebase)

## Common Tasks
- **Adding new flashcards**: Edit the `text` string in `prompt.py`
- **Modifying UI**: Update widget properties in `main.py` setup section (lines 75-126)
- **Processing selections**: Use `get_selected_content(checkbox_save)` pattern
- **Adding buttons**: Follow the `button_frame` pattern with consistent styling

## File Organization
- Keep data separate from UI logic
- One function per file for utilities
- Main file handles all GUI setup and event binding</content>
<parameter name="filePath">d:\Python Zeugs\Karteikarten in csv\.github\copilot-instructions.md