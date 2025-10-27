class Contact:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        # Check if the phone number already exists in the contacts list
        for existing_contact in self.contacts:
            if existing_contact.phone == contact.phone:
                print("Error: Duplicate phone number.")
                return False
        
        # If no duplicate is found, add the new contact
        self.contacts.append(contact)
        return True
    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        for contact in self.contacts:
            print(contact)

    def remove_contact(self, phone):
        # Create a new list to store contacts that do not match the phone number
        updated_contacts = []
        
        # Iterate over each contact in the current contacts list
        for contact in self.contacts:
            # If the contact's phone number does not match the given phone number, keep it
            if contact.phone == phone:
                pass
            else:
                updated_contacts.append(contact)
        
        # Update the contacts list with the filtered contacts
        self.contacts = updated_contacts