import json
from datetime import datetime, timedelta
import pickle

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

    def handle_hello():
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
        with open(filename, "wb+") as file:
            pickle.dump(self.contacts, file)

    def load_contacts(self, filename):
        try:
           with open(filename, 'rb') as file:
             self.contacts = pickle.load(file)
        except FileNotFoundError:
                self.contacts = []


def handle_add():
    name = input("Enter the name: ")
    address = input("Enter the address: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email: ")
    birthday = input("Enter the birthday (YYYY-MM-DD): ")
    AddressBook.handle_add(name, address, phone, email, birthday)
    AddressBook.save_contacts("usersbook.pkl")
    print("Contact added successfully.")

def handle_change():
    name = input("Enter the name of the contact to change: ")
    address = input("Enter the new address: ")
    phone = input("Enter the new phone number: ")
    email = input("Enter the new email: ")
    birthday = input("Enter the new birthday (YYYY-MM-DD): ")
    AddressBook.handle_change(name, address, phone, email, birthday)
    AddressBook.save_contacts("usersbook.pkl")

    print("Contact change successfully.") 

def handle_search():
    search_term = input("Enter the search term: ")
    AddressBook.handle_delete(search_term)
    print(f'{AddressBook.handle_search(search_term)}')

def handle_delete():
    name = input("Enter the name of the contact to delete: ")
    if Contact.name == name:
        AddressBook.handle_delete(name)
        AddressBook.save_contacts("usersbook.pkl")
        print("Contact delete successfully.") 
    else:
         print("Invalid note Name.")


def get_upcoming_birthdays(days):
    days = int(input("Enter the number of days to check: "))
    print (f'{AddressBook.get_upcoming_birthdays(days)}')

def save_contacts():
    AddressBook.save_contacts("usersbook.pkl")

def load_contacts():
    AddressBook.load_contacts("usersbook.pkl")



def main():
            
        global AddressBook
        AddressBook = AddressBook() 
        load_contacts()
            
        while True:
            print('Menu AddressBook:')
            print('1. Contact add')
            print('2. change a Contact')
            print('3. Delete a Contact')
            print('4. Search Contact')
            print('5.  birthdays in the coming days')
            print('6. or "good bye", "close", "exit" for close Contact')
            print('7. Save Contact')
            print('8. Loaded Contact')

            command = input("Enter a command: ").lower()
            if command == "hello":
                print ('I see You!!! Poot command)))))) ')
               
            elif command == "1":
                handle_add()
           
            elif command == "2":
                handle_change()
               
            elif command == "3":
                handle_delete()
                
            elif command == "4":
                handle_search()

            elif command == "7":
                save_contacts()
                print("Contacts saved successfully.")
            elif command == "8":
                load_contacts()
                print ("Contacts loaded successfully.")

            elif command == "5":
               get_upcoming_birthdays()
            
            elif command in ["good bye", "close", "exit"]:
                save_contacts()
                print("Good bye!")
                break
            else:
               print ("Invalid command.")
             


if __name__ == "__main__":
    main()