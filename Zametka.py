import json
from datetime import datetime

filename = 'notes.json'

def load_notes():
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_notes(notes):
    with open(filename, 'w') as f:
        json.dump(notes, f, indent=4, default=str)

def add_note():
    title = input("Vvedite zagolovok ")
    message = input("Vvedite telo ")
    note = {
        "id": len(load_notes()) + 1,
        "title": title,
        "message": message,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    print("Zametka soxranena")

def edit_note():
    try:
        note_id = int(input("Vvedite ID dlya redaktirovaniya "))
        title = input("Vvedite noviy zagolovok ")
        message = input("Vvedite novoe telo ")
        
        notes = load_notes()
        for note in notes:
            if note["id"] == note_id:
                if title:
                    note["title"] = title
                if message:
                    note["message"] = message
                note["date"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                save_notes(notes)
                print("Zametka obnovlena")
                return
        print("Zametka s takim ID ne naidena")
    except ValueError:
        print("ERROR, ID doljno bit chislom")
       
def delete_note():
    # list_notes()
    try:
        note_id = int(input("Vvedite ID zametki dlya udaleniya "))
        
        notes = load_notes()
        notes = [note for note in notes if note["id"] != note_id]
        save_notes(notes)
        print("Zametka udalena")
    except ValueError:
        print("ERROR, ID dojlno bit chislom")

def list_notes():
    notes = load_notes()
    for note in notes:
        print(f'{note["id"]}. {note["title"]} ({note["date"]}): {note["message"]}')

def main():
    while True:
        cmd = input("Vvedite komandu (add, edit, delete, list, exit): ")
        if cmd == "add":
            add_note()
        elif cmd == "list":
            list_notes()
        elif cmd == "edit":
            edit_note()
        elif cmd == "delete":
            delete_note()       
        elif cmd == "exit":
            break
        else:
            print("ERROR")

if __name__ == "__main__":
    main()