class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number):
        self.contacts[name] = phone_number
        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("Contact List:")
            for name, phone_number in self.contacts.items():
                print(f"{name}: {phone_number}")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"{name}: {self.contacts[name]}")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully!")
        else:
            print(f"Contact {name} not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            contact_book.add_contact(name, phone_number)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            name = input("Enter contact name to search: ")
            contact_book.search_contact(name)
        elif choice == "4":
            name = input("Enter contact name to delete: ")
            contact_book.delete_contact(name)
        elif choice == "5":
            print("Exiting contact book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
