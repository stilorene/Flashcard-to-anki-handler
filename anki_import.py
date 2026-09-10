import requests


def get_anki_decks():
    """Holt eine Liste aller Decks, die aktuell in Anki existieren."""
    url = "http://localhost:8765"
    payload = {
        "action": "deckNames",
        "version": 6
    }

    try:
        response = requests.post(url, json=payload, timeout=3).json()
        print(response)

        if response.get("error"):
            print(f"Fehler beim Abrufen der Decks: {response['error']}")
            return []
        return response.get("result", [])  # Gibt eine Liste mit Namen zurück, z.B. ["Default", "Spanisch", "Python"]
    except requests.exceptions.ConnectionError:
        ROT = "\033[91m"
        RETURN = "\033[0m"
        print(f"{ROT}Konnte keine Verbindung zu Anki herstellen. Bitte stelle sicher, dass Anki geöffnet ist und das AnkiConnect-Plugin installiert ist.{RETURN}")
        return []


def create_anki_deck(deck_name):
    """Erstellt in Anki einen neuen Stapel."""
    cleaned_name = (deck_name or "").strip()

    if not cleaned_name:
        print("Kein Stapelname angegeben.")
        return False

    url = "http://localhost:8765"
    payload = {
        "action": "createDeck",
        "version": 6,
        "params": {
            "deck": cleaned_name
        }
    }

    try:
        response = requests.post(url, json=payload, timeout=3).json()
        print(response)

        if response.get("error"):
            print(f"Fehler beim Erstellen des Stapels: {response['error']}")
            return False

        return True
    except requests.exceptions.ConnectionError:
        ROT = "\033[91m"
        RETURN = "\033[0m"
        print(f"{ROT}Konnte keine Verbindung zu Anki herstellen. Bitte stelle sicher, dass Anki geöffnet ist und das AnkiConnect-Plugin installiert ist.{RETURN}")
        return False


if __name__ == "__main__":
    get_anki_decks()
