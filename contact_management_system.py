import re
import os

def valid_email(email):
    '''This function takes a string and returns True if it's a valid email and False otherwise'''
    if re.search(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$", email):
        return True
    else:
        return False

def valid_phone_number(num):
    '''This function takes a string and returns True if it's a valid phone number and False otherwise'''
    if re.search(r"^\d{3}-\d{3}-\d{4}$", num):
        return True
    else:
        return False

def valid_name(name):
    '''This function takes a string and returns True if it's a valid name (no numbers or special characters) and False otherwise'''
    if re.search(r"^[A-Za-z\s]+$", name):
        return True
    else:
        return False

def valid_address(address):
    '''This function takes a string and returns True if it's a valid address (no numbers or special characters) and False otherwise'''
    if re.search(r"^[A-Za-z0-9.,\s\n]+$", address):
        return True
    else:
        return False

def validate_info(num):
    '''With the parameter of an int(1-5), this function will prompt the user to input the attribute 
    and if it's not valid, prompt again.'''
    # Name = 1
    if num == 1:
        info = input("\nEnter contact's name:\n")
        while not valid_name(info):
            print("\nThis name is not valid, try again.")
            info = input("\nEnter contact's name:\n")
    # Phone Number = 2
    elif num == 2:  
        info = input("\nEnter contact's phone (###-###-####):\n")
        if not valid_phone_number(info):
            print("\nThis phone is not valid, try again.")
            info = input("\nEnter contact's phone (###-###-####):\n")
    # Email = 3
    elif num == 3:  
        info = input("\nEnter contact's email (username@domain.com):\n")
        while not valid_email(info):
            print("\nThis email is not valid, try again.")
            info = input("\nEnter email (username@domain.com):\n")
    # Address = 4
    elif num == 4:
        info = input("\nEnter contact's address (no special characters):\n")
        while not valid_address(info):
            print("\nThis address is not valid, try again.")
            info = input("\nEnter contact's address (no special characters):\n")
    # Notes = 5
    elif num == 5:
        info = input("\nEnter any additional notes:\n")
    return info

def add_contact(contacts, name, phone, email, address, notes): 
    '''This function takes the contacts dictionary and adds a new name key, 
    with phone, email, address, and notes as its values'''
    if name not in contacts: 
        contacts[name] = [phone, email, address, notes]
        print(f"\nThe contact '{name}' has been added to the system.")
    # If the name doesn't exists in the dictionary, alerts user
    else: 
        print(f"\nThe contact '{name}' already exists in the system.")

def edit_contact(contacts):
    # If contacts is empty, alert user
    if contacts == {}: 
        print("\nThe Contact Management System is empty.")
    else: 
        # Display the contacts in numbered format for user to choose which to edit
        display_contacts(contacts)
        try:
            # Prompt the user for which to edit
            contact_index = int(input(f"\nPlease choose which contact you'd like to edit: "))
            # Raise error if invalid input
            if contact_index > len(contacts) or contact_index <=0:
                raise ValueError()
            elif contact_index==len(contacts):
                contact_index = 0
            # Retrieve name based on the user input
            contact_name = list(contacts.keys())[contact_index]
            # Display the attributes that can be edited
            print("\n1. Name\n2. Phone Number\n3. Email Address\n4. Address\n5. Notes")
            # Prompt the user for their choice of attribute
            attribute_index = int(input("\nPlease select what category you'd like to edit (1-5): \n"))
            # Raise error if invalid input
            if attribute_index > 5 or attribute_index <=0:
                raise ValueError
            # Prompt user for the updated information
            new_info = validate_info(attribute_index)
            # If the attribute they'd like to change is the name
            if attribute_index == 1:
                # Replace old entry with new entry
                contacts[new_info] = contacts.pop(contact_name)
                print(f"\nThe contact {new_info} has been updated.")
            # Update the attribute with the new information
            else:
                contacts[contact_name][attribute_index-2] = new_info
                print(f"\nThe contact {contact_name} has been edited.")
        except ValueError:
            print("\nInvalid input.")
        except Exception as e:
            print(f"\nAn error occurred: {e}.")

def delete_contact(contacts):
    '''This function takes the contact list, displays it to the user and allows them to choose which contact to delete.'''
    # If the contact list is empty, alert user.
    if contacts == {}: 
        print("\nThe Contact Management System is empty.")
    else: 
        # Display the contacts in numbered format for user to choose which to edit
        display_contacts(contacts)
        try:
            # Prompt the user for which contact to be deleted
            contact_index = int(input(f"\nPlease choose which contact you'd like to delete: \n"))
            # Raise error for invalid input
            if contact_index > len(contacts) or contact_index <=0:
                raise ValueError()
            elif contact_index==len(contacts):
                contact_index = 0
            # Retrieve name based on the user input
            # Retrieve contact name
            contact_name = list(contacts.keys())[contact_index]
            # Remove contact from list
            contacts.pop(contact_name)
            print(f"\nThe contact '{contact_name}' has been deleted from the system.")
        except ValueError:
            print("\nInvalid input.")
        except Exception as e:
            print(f"\nAn error occurred: {e}.")

def search_contacts(contacts, name):
    '''This function takes the contact list and a name and searches the list for the contact.'''
    found = False
    for contact, values in contacts.items():
        if name.lower() == contact.lower():
            found = True
            name, phone, email, address, notes = contact, values[0], values[1], values[2], values[3]
    if found:
        print(f"\nWe found the following contact information:\nName: {name}\nPhone Number: {phone}\nEmail Address: {email}\nAddress: {address}\nNotes: {notes}")
    else:
        print(f"\nThe contact '{name}' is not in the system.")


def display_contacts(contacts):
    '''This function takes a dictionary and displays the content'''
    # Inform user if the dictionary is empty
    if contacts == {}:
        print("\nThe Contact Management System is empty.")
    else:
        # Iterate over the contacts
        for i, contact in enumerate(sorted(contacts)):
            # Print out the information in a user-friendly way
            print(f'''
{i+1}. Name: {contact}
   Phone Number: {contacts[contact][0]}
   Email Address: {contacts[contact][1]}
   Address: {contacts[contact][2]}
   Notes: {contacts[contact][3]}
''')

def export_contacts(contacts, path, filename):
    '''This function takes the dictionary of contacts and exports them to a given filename in a path location.
    Saved as: "name:phone_number,email_address,address,notes" on each line'''
    try:
        # If the contact list is empty, informs user
        if contacts == {}:
            print("\nThe Contact Management System is empty, nothing to export!")
        # If the path does not exist, raise error
        elif not os.path.exists(path):
            raise FileNotFoundError()
        else:
            # Opening the path (if it already exists, overwrite it)
            with open(path+"/"+filename, 'w') as file:
                # Iterates over the keys and writes them to the file
                for key, values in contacts.items():
                    file.write(f"{key}:{values[0]},{values[1]},{values[2]},{values[3]}\n")
            # Informs the user that it's been exported
            print(f"The Contact Management System has been exported with the filename: {filename}")
    except FileNotFoundError:
        print("The path and/or file were not valid. Try again.")
    except Exception as e:
        print(f"An error occurred: {e}.")
        
def import_contacts(contacts, path):
    '''This function takes the contact list (empty or not) and a filename path with more contacts and imports them
    File contact format should be: "name:phone_number,email_address,address,notes" on each line'''
    try:
        # If path does not exist, raise error
        if not os.path.exists(path):
            raise FileNotFoundError()
        else:
            # Opens the file and iterates over the lines, saving them in the contacts list
            with open(path, 'r') as file:
                for line in file:
                    key, values = line.strip().split(':')
                    phone, email, address, notes = values.split(",")
                    contacts[key] = [phone, email, address, notes]
            # Inform the user
            print(f"\nThe contacts were imported from {path}.")
    except FileNotFoundError:
        print("Could not import file because it was not found. Try again.")
    except Exception as e:
        print(f"An error occurred: {e}.")

def main():
    # Welcome the user
    print("\nWelcome to the Contact Management System!")
    # Create the contact list
    all_contacts = {}
    while True:
        try: 
            # MAIN MENU
            print('''
Menu:
1. Add a New Contact
2. Edit an Existing Contact
3. Delete a Contact
4. Search for a Contact
5. Display All Contacts
6. Export Contacts to a Text File
7. Import Contacts from a Text File
8. Quit
            ''')
            # Prompt user for their menu item
            i = int(input("Please enter a menu item: "))
            # 1 = Add Contact
            if i == 1:
                # Prompt user for name, phone number, email address, address, and notes
                name, phone, email, address, notes = validate_info(1), validate_info(2), validate_info(3), validate_info(4), validate_info(5)
                add_contact(all_contacts, name, phone, email, address, notes)
            # 2 = Edit Contact
            elif i == 2:
                edit_contact(all_contacts)
            # 3 = Delete Contact
            elif i == 3:
                delete_contact(all_contacts)
            # 4 = Search Contacts
            elif i == 4:
                # Prompt user for name
                name = validate_info(1)
                search_contacts(all_contacts, name)
            # 5 = Display Contacts
            elif i == 5:
                display_contacts(all_contacts)
            # 6 = Export Contacts
            elif i == 6:
                # Prompt user for file path and name
                filepath = input("Please input a file path: \n")
                filename = input("Please input a file name: \n")
                export_contacts(all_contacts, filepath, filename)
            # 7 = Import Contacts
            elif i == 7:
                # Prompt user for file name path
                filename = input("Please input a file name path to import from: \n")
                import_contacts(all_contacts, filename)
            # 8 = Exit
            elif i == 8:
                # Thank the user and exit
                print("Have a great day, good-bye!")
                break
            # If given a different number, raise error
            else: 
                raise ValueError()
        except ValueError:
            print("Please enter a valid menu item (1-8).")
        except Exception as e:
            print(f"An error occurred: {e}.")
    
if __name__ == "__main__":
    main()