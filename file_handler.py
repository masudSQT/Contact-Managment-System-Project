import json
from contact import Contact

filename='contacts.json'
def save_contacts_to_file(contacts):
    # Open the specified file in write mode
    with open(filename, 'w') as file:
        # Create a list to store contact dictionaries
        contact_list = []
        
        # Convert each contact object to a dictionary and add it to the list
        for contact in contacts:
            contact_dict = contact.__dict__
            contact_list.append(contact_dict)
        
        # Write the list of contact dictionaries to the file in JSON format
        json.dump(contact_list, file, indent=4)

def load_contacts_from_file():
    # Initialize an empty list to store contacts
    contacts = []

    # Try to open the specified file
    try:
        with open(filename, 'r') as file:
            # Try to load the JSON data from the file
            try:
                json_contacts = json.load(file)
        
                # Convert each dictionary in the JSON data to a Contact object
                # Assume json_contacts is a list of dictionaries, each representing a contact

                # Loop through each contact dictionary in the JSON data
                for contact_data in json_contacts:
                    # Create a Contact object using the dictionary data
                    contact = Contact(
                        name=contact_data['name'],
                        email=contact_data['email'],
                        phone=contact_data['phone'],
                        address=contact_data['address']
                    )
                    
                    # Add the Contact object to the contacts list
                    contacts.append(contact)
            except json.JSONDecodeError:
                # Handle the case where the JSON data is invalid
                print("Warning: JSON file is empty or corrupted. Starting with an empty contact list.")
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print("Warning: JSON file not found. Starting with an empty contact list.")

    # Return the list of contacts
    return contacts