# Create an empty dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    emailaddress = input("Enter the email address: ")
    address = input("Enter the address: ")
    contacts[name] = {
        'phone': phone,
        'email address': emailaddress,
        'address': address
    }
    print(f"Contact for {name} added successfully!")

# Function to display a list of saved contacts with names and phone numbers
def display_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for name, contact in contacts.items():
            print(f"Name: {name}, Phone: {contact['phone']}")

# Function to update a contact
def update_contact(name):
    if name in contacts:
        phone = input("Enter the new phone number: ")
        email = input("Enter the new email: ")
        address = input("Enter the new address: ")
        contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print(f"Contact for {name} updated successfully!")
    else:
        print(f"Contact for {name} not found!")

# Function to delete a contact
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact for {name} deleted successfully!")
    else:
        print(f"Contact for {name} not found!")

# Main menu
while True:
    print("\nContacts Menu:")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        display_contacts()
    elif choice == '3':
        name = input("Enter the name of the contact to update: ")
        update_contact(name)
    elif choice == '4':
        name = input("Enter the name of the contact to delete: ")
        delete_contact(name)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")