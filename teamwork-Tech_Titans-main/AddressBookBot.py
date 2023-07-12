import json
from datetime import datetime, timedelta


class Contact:
    def __init__(self, name, address, phone, email, birthday):
        self.name = name
        self.address = address
        self.__phone = phone
        self.__email = email
        self.birthday = birthday

    def to_dict(self):
        return {
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
            "birthday": self.birthday
        }

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if not isinstance(phone, str):
            raise ValueError("Phone number must be a string")
        if not phone.isdigit():
            raise ValueError("Phone number must contain only digits")
        if len(phone) != 10:
            raise ValueError("Phone number must be 10 digits long")
        self.__phone = phone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        exceptions = [";", ",", "[", "]", "*", "(", ")", ">", "<", ":"]
        for i in exceptions:
            if email.find(i) != -1:
                raise ValueError("Mail contains prohibited characters")

        if "@" not in email and "." not in email:
            raise ValueError("Email must contain the @ symbol")
        if email[0] == "@" or email[-1] == "@":
            raise ValueError("The @ symbol cannot be the first or last character")
        if email.count("@") > 1:
            raise ValueError("The @ symbol must be only one")
        self.__email = email


class AddressBook:
    def __init__(self):
        self.contacts = []

    def search_contacts(self, search_term):
        results = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term.lower() in contact.phone.lower():
                results.append(contact)
        return results

    def edit_contact(self, old_name, new_name, new_email, new_phone, new_favorite):
        for contact in self.contacts:
            if contact.name == old_name:
                contact.name = new_name
                contact.email = new_email
                contact.phone = new_phone
                contact.favorite = new_favorite
                return True
        return False

    def get_upcoming_birthdays(self, days):
        today = datetime.now().date()
        upcoming_birthdays = []

        for contact in self.contacts:
            birthday = datetime.strptime(contact.birthday, "%Y-%m-%d").date()
            upcoming_birthday = birthday.replace(year=today.year)

            if today <= upcoming_birthday <= today + timedelta(days=days):
                upcoming_birthdays.append(contact)

        return upcoming_birthdays

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return True
        return False

    def handle_hello(self):
        return "How can I help you?"

    def handle_add(self, name, address, phone, email, birthday):
        try:
            contact = Contact(name, address, phone, email, birthday)
            self.contacts.append(contact)
            return "Contact added successfully."
        except ValueError as e:
            return str(e)

    def handle_change(self, name, address, phone, email, birthday):
        for contact in self.contacts:
            if contact.name == name:
                try:
                    contact.address = address
                    contact.phone = phone
                    contact.email = email
                    contact.birthday = birthday
                    return "Contact updated successfully."
                except ValueError as e:
                    return str(e)
        return "Contact not found."

    def handle_delete(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return "Contact deleted successfully."
        return "Contact not found."

    def handle_search(self, search_term):
        results = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term.lower() in contact.phone.lower():
                results.append(contact)
        if results:
            return results
        else:
            return "No contacts found."

    def save_contacts(self, filename):
        with open(filename, "w") as file:
            json.dump([contact.to_dict() for contact in self.contacts], file)

    def load_contacts(self, filename):
        try:
            with open(filename, "r") as file:
                contacts_data = json.load(file)
                self.contacts = [Contact(**data) for data in contacts_data]
        except FileNotFoundError:
            self.contacts = []


def handle_add():
    name = input("Enter the name: ")
    address = input("Enter the address: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email: ")
    birthday = input("Enter the birthday (YYYY-MM-DD): ")
    address_book.handle_add(name, address, phone, email, birthday)
    address_book.save_contacts("usersbook.json")
    print("Contact added successfully.")


def handle_change():
    name = input("Enter the name of the contact to change: ")
    address = input("Enter the new address: ")
    phone = input("Enter the new phone number: ")
    email = input("Enter the new email: ")
    birthday = input("Enter the new birthday (YYYY-MM-DD): ")
    address_book.handle_change(name, address, phone, email, birthday)
    address_book.save_contacts("usersbook.json")
    print("Contact changed successfully.")


def handle_search():
    search_term = input("Enter the search term: ")
    results = address_book.handle_search(search_term)
    if isinstance(results, list):
        for contact in results:
            print(contact.to_dict())
    else:
        print(results)


def handle_delete():
    name = input("Enter the name of the contact to delete: ")
    result = address_book.handle_delete(name)
    if result:
        address_book.save_contacts("usersbook.json")
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def get_upcoming_birthdays():
    days = int(input("Enter the number of days to check: "))
    results = address_book.get_upcoming_birthdays(days)
    for contact in results:
        print(contact.to_dict())


def save_contacts():
    address_book.save_contacts("usersbook.json")
    print("Contacts saved successfully.")


def load_contacts():
    address_book.load_contacts("usersbook.json")
    print("Contacts loaded successfully.")


def main():
    global address_book
    address_book = AddressBook()
    load_contacts()

    while True:
        print("Menu AddressBook:")
        print("1. Contact add")
        print("2. Change a Contact")
        print("3. Delete a Contact")
        print("4. Search Contact")
        print("5. Birthdays in the coming days")
        print('6. Or "good bye", "close", "exit" to close AddressBook')
        print("7. Save Contacts")
        print("8. Load Contacts")

        command = input("Enter a command: ").lower()

        if command == "1":
            handle_add()

        elif command == "2":
            handle_change()

        elif command == "3":
            handle_delete()

        elif command == "4":
            handle_search()

        elif command == "5":
            get_upcoming_birthdays()

        elif command == "6" or command in ["good bye", "close", "exit"]:
            save_contacts()
            print("Good bye!")
            break

        elif command == "7":
            save_contacts()

        elif command == "8":
            load_contacts()

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
