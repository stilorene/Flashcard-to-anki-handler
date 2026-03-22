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
        return response.get("result", []) # Gibt eine Liste mit Namen zurück, z.B. ["Default", "Spanisch", "Python"]
    except requests.exceptions.ConnectionError:
        print("Konnte keine Verbindung zu Anki herstellen.")
        return []
    

#Anzeigen lassen welche Stapel schon exestieren





get_anki_decks()