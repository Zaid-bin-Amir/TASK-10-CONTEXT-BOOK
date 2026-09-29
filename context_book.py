"""
Level 1 - Day 10: Contact Book Using Dictionaries
CRUD operations (Create, Read/Search, Update, Delete) on contacts.

Data structure:
    contacts = {
        "phone_number": {"name": ..., "email": ..., "city": ...},
    }
The phone number is the key, so duplicates are easy to detect.
"""

# Sample contact data
contacts = {
    "03001234567": {"name": "Ali Khan", "email": "ali@example.com", "city": "Lahore"},
    "03111234567": {"name": "Sara Ahmed", "email": "sara@example.com", "city": "Sargodha"},
    "03211234567": {"name": "Usman Tariq", "email": "usman@example.com", "city": "Karachi"},
}


def is_valid_phone(phone):
    """Phone must be digits only and 10-13 characters long."""
    return phone.isdigit() and 10 <= len(phone) <= 13


def print_contact(phone, info):
    print(f"  Phone : {phone}")
    print(f"  Name  : {info['name']}")
    print(f"  Email : {info['email']}")
    print(f"  City  : {info['city']}")
    print("  " + "-" * 30)


def add_contact():
    phone = input("Enter phone number: ").strip()
    if not is_valid_phone(phone):
        print("Invalid phone number. Use digits only (10-13 digits).")
        return
    if phone in contacts:  # duplicate validation
        print("A contact with this phone number already exists.")
        return
    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    email = input("Enter email: ").strip()
    city = input("Enter city: ").strip()
    contacts[phone] = {"name": name, "email": email, "city": city}
    print(f"Contact '{name}' added successfully.")


def view_all():
    if not contacts:
        print("Contact book is empty.")
        return
    print(f"\nTotal contacts: {len(contacts)}")
    for phone, info in contacts.items():
        print_contact(phone, info)


def search_contact():
    term = input("Search by name or phone: ").strip().lower()
    found = False
    for phone, info in contacts.items():
        if term in phone or term in info["name"].lower():
            print_contact(phone, info)
            found = True
    if not found:
        print("No matching contact found.")


def update_contact():
    phone = input("Enter phone number of contact to update: ").strip()
    if phone not in contacts:
        print("Contact not found.")
        return
    info = contacts[phone]
    print("Leave a field blank to keep the current value.")
    name = input(f"New name [{info['name']}]: ").strip()
    email = input(f"New email [{info['email']}]: ").strip()
    city = input(f"New city [{info['city']}]: ").strip()
    if name:
        info["name"] = name
    if email:
        info["email"] = email
    if city:
        info["city"] = city
    print("Contact updated successfully.")


def delete_contact():
    phone = input("Enter phone number of contact to delete: ").strip()
    if phone not in contacts:
        print("Contact not found.")
        return
    confirm = input(f"Delete {contacts[phone]['name']}? (y/n): ").strip().lower()
    if confirm == "y":
        del contacts[phone]
        print("Contact deleted.")
    else:
        print("Deletion cancelled.")


def show_menu():
    print("\n===== CONTACT BOOK =====")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")


def main():
    actions = {
        "1": add_contact,
        "2": view_all,
        "3": search_contact,
        "4": update_contact,
        "5": delete_contact,
    }
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == "6":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()