from contact import Contact, ContactBook
from file_handler import save_contacts_to_file, load_contacts_from_file

def main():
    contact_book = ContactBook()
    contact_book.contacts = load_contacts_from_file()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            address = input("Enter address: ")
            contact = Contact(name, email, phone, address)
            if contact_book.add_contact(contact):
                save_contacts_to_file(contact_book.contacts)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            phone = input("Enter phone number to remove: ")
            contact_book.remove_contact(phone)
            save_contacts_to_file(contact_book.contacts)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()