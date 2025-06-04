# A Contacts Management Program by me. Enjoy!Add commentMore actions

def display_menu():
    print("Contact Book Menu:\n1. Add Contact\n2. View Contact\n3. Edit Contact\n4. Delete Contact\n5. List All Contacts\n6. Exit")

def add_contact(contact_book: dict) -> str:
    name, phone, email, address = input(), input(), input(), input()
    if name not in contact_book:
        contact_book.update({name:{"phone": phone,
                                   "email": email,
                                   "address": address}})
        print("Contact added successfully!")
    else:
        print("Contact already exists!")

def view_contact(contact_book: dict) -> str:
    contact_name = input()
    if contact_name in contact_book:
        print(f"Name: {contact_name}")
        print(f"Phone: {contact_book[contact_name]["phone"]}")
        print(f"Email: {contact_book[contact_name]["email"]}")
        print(f"Address: {contact_book[contact_name]["address"]}")
    else:
        print("Contact not found!")

def edit_contact(contact_book: dict) -> str:
    contact_name = input()
    if contact_name in contact_book:
        new_phone, new_email, new_address = input(), input(), input()
        if new_phone:
            contact_book[contact_name]["phone"] = new_phone
        if new_email:
            contact_book[contact_name]["email"] = new_email
        if new_address:
            contact_book[contact_name]["address"] = new_address
        else:
            pass
        print("Contact updated successfully!")
    else:
        print("Contact not found!")    

def delete_contact(contact_book: dict) -> str: 
    contact_name = input()
    if contact_name in contact_book:
        del contact_book[contact_name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")
    
def list_all_contacts(contact_book: dict) -> str:
    if not contact_book:
        print("No contacts available.")
    else:
        for name, info in contact_book.items():
            print(f"Name: {name.capitalize()}")
            for k, v in info.items():
                print(f"{k.capitalize()}: {v}")
            print()

contact_book = {}

while True:
    choice = ""
    display_menu()
    choice = input()
    if choice == "1":
        add_contact(contact_book)
    elif choice == "2":
        view_contact(contact_book)
    elif choice == "3":
        edit_contact(contact_book)
    elif choice == "4":
        delete_contact(contact_book)
    elif choice == "5":
        list_all_contacts(contact_book)
    elif choice == "6":
        quit()
