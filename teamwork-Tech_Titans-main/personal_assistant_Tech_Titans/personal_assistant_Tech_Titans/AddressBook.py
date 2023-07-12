import json
from datetime import datetime, timedelta


class Contact:
    def __init__(self, name, address, phone, email, birthday):
        self.name = name
        self.address = address
        self.__phone = phone
        self.__email = email
        self.birthday = birthday

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
        exceptions = [";", ',', "[", "]", "*",
                      "(", ")", ">", "<", ":"]
        for i in exceptions:
            if email.find(i) != -1:
                raise ValueError("Mail contains prohibited characters")

        if "@" not in email and "." not in email:
            raise ValueError("Email must contain the @ symbol")
        if email[0] == "@" or email[-1] == "@":
            raise ValueError(
                "The @ symbol cannot be the first or last character")
        if email.count('@') > 1:
            raise ValueError("The @ symbol must be only one ")
        self.__email = email

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

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return True
        return False


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def save_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.contacts, file)

    def load_file(self, filename):
        with open(filename, 'r') as file:
            self.contacts = json.load(file)

    def get_upcoming_birthdays(self, days):
        today = datetime.now().date()
        upcoming_birthdays = []

        for contact in self.contacts:
            birthday = datetime.strptime(contact.birthday, "%Y-%m-%d").date()
            upcoming_birthday = birthday.replace(year=today.year)

            if today <= upcoming_birthday <= today + timedelta(days=days):
                upcoming_birthdays.append(contact)

        return upcoming_birthdays

