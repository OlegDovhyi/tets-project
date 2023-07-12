import json
from datetime import datetime


class Note:
    def __init__(self, name, content, tags=None):
        self.name = name
        self.content = content
        self.tags = tags if tags else []
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    def set_name(self, new_name):
        self.name = new_name

    def add_tag(self, tag):
        self.tags.append(tag)

    def remove_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)

    def search_by_tag(self, tag):
        matching_notes = []
        if tag in self.tags:
            matching_notes.append(self)
        return matching_notes

    def to_dict(self):
        return {
            "name": self.name,
            "content": self.content,
            "tags": self.tags,
            "timestamp": self.timestamp
        }


class NoteBook:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def search_notes(self, keyword):
        found_notes = []
        for note in self.notes:
            if keyword.lower() in note.content.lower():
                found_notes.append(note)
        return found_notes

    def edit_note(self, index, note):
        if 0 <= index < len(self.notes):
            self.notes[index] = note
        else:
            raise IndexError("Invalid note index")

    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            del self.notes[index]
        else:
            raise IndexError("Invalid note index")

    def search_notes_by_tag(self, tag):
        matching_notes = []
        for note in self.notes:
            if tag in note.tags:
                matching_notes.append(note)
        return matching_notes

    def save_notes(self, filename):
        notes_data = [note.to_dict() for note in self.notes]
        with open(filename, "w") as file:
            json.dump(notes_data, file)
        print('Notes saved successfully.')

    def load_notes(self, filename):
        try:
            with open(filename, "r") as file:
                notes_data = json.load(file)
                self.notes = [Note(**data) for data in notes_data]
        except FileNotFoundError:
            self.notes = []


def add_note():
    name = input("Enter the note name: ")
    content = input("Enter the note content: ")
    tags = input("Enter tags for the note: ")
    if tags:
        tags = [tag.strip() for tag in tags.split(",")]
    note = Note(name, content, tags)
    notebook.add_note(note)
    notebook.save_notes("usernotes.json")
    print("Note added successfully.")
    print("Timestamp:", note.timestamp)


def edit_note():
    index = int(input("Enter the index of the note to edit: "))
    if 0 <= index < len(notebook.notes):
        note = notebook.notes[index]
        new_name = input("Enter the new name for the note: ")
        content = input("Enter the new content for the note: ")
        tags = input("Enter new tags for the note (comma-separated, press Enter to skip): ")
        if tags:
            tags = [tag.strip() for tag in tags.split(",")]
        note.set_name(new_name)  
        note.content = content
        note.tags = tags
        notebook.edit_note(index, note)
        notebook.save_notes("usernotes.pkl")
        print("Note edited successfully.")
    else:
        print("Invalid note index.")



def delete_note():
    index = int(input("Enter the index of the note to delete: "))
    if 0 <= index < len(notebook.notes):
        notebook.delete_note(index)
        notebook.save_notes("usernotes.json")
        print("Note deleted successfully.")
    else:
        print("Invalid note index.")


def search_notes():
    keyword = input("Enter a keyword to search notes: ")
    found_notes = notebook.search_notes(keyword)
    if found_notes:
        print("Found notes:")
        for note in found_notes:
            print(f"Name: {note.name}")
            print(f"Content: {note.content}")
            print(f"Tags: {', '.join(note.tags)}")
            print()
    else:
        print("No notes found.")


def search_notes_by_tag():
    tag = input("Enter a tag to search notes: ")
    matching_notes = notebook.search_notes_by_tag(tag)
    if matching_notes:
        print("Matching notes:")
        for note in matching_notes:
            print(f"Name: {note.name}")
            print(f"Content: {note.content}")
            print(f"Tags: {', '.join(note.tags)}")
            print()
    else:
        print("No notes found with this tag.")


def load_notes():
    notebook.load_notes("usernotes.json")

def save_notes():
    notebook.save_notes("usernotes.json")


def main():
    global notebook
    notebook = NoteBook()
    notebook.load_notes("usernotes.json")

    while True:
        print('Menu:')
        print('1. Add a note')
        print('2. Edit a note')
        print('3. Delete a note')
        print('4. Search notes')
        print('5. Search notes by tag')
        print(' "6" or "good bye", "close", "exit" for close NoteBook')
        print('7. Save notes')

        choice = input('Enter the option number: ')

        if choice == '1':
            add_note()
        elif choice == '2':
            edit_note()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            search_notes()
        elif choice == '5':
            search_notes_by_tag()
        elif choice == '7':
           save_notes()
           
        elif choice == '6':
            save_notes()
            break
        elif choice in ["good bye", "close", "exit"]:
            save_notes()
            break
        else:
            print('Invalid input. Please try again.')


if __name__ == "__main__":
    main()
# users_NoteBook