# Module 3 - Mini-Project - Contact Management System
Author: Elizabeth Yates

The Contact Management System has eight features, as shown on the main menu. 

## Main Menu

Menu:
1. Add a New Contact
2. Edit an Existing Contact
3. Delete a Contact
4. Search for a Contact
5. Display All Contacts
6. Export Contacts to a Text File
7. Import Contacts from a Text File
8. Quit
  
- At the menu, the user will be prompted to choose an option by selecting a number. 
- If they select a number out of the range (1-8) or input a word, they will be reminded that that's not a valid input and prompted again. 

## 1. Add a New Contact
- This option will allow the user to input a unique contact to add to the list.
- First the user will be prompted to provide the contact's name, phone number, email address, address and any additional notes. The user must give a valid input or else they will be prompted again. Here are the format requirements: 
    - Name: No numbers or special characters
    - Phone Number: ###-###-####
    - Email Address: username@domain.com
    - Address: No special characters
    - Notes: No requirements
- The user will be alerted that the contact's been added to the list.
- If the contact is already on the list, the user will be alerted and brought back to the main menu. 

## 2. Edit an Existing Contact
- This option will allow the user to edit an existing contact. 
- It will first display the contacts in a numbered list and then prompt the user to choose which contact. 
- If the user gives a number out of range or a string, it will alert the user and bring them back to the main menu. 
- It will then display the attribute that the user would like to edit: 
    1. Name  
    2. Phone Number  
    3. Email Address  
    4. Address  
    5. Notes
- Again, a user will be informed of an invalid input. 
- The contact's information will then be updated and the user notified. 

## 3. Delete a Contact
- This option will allow the user to delete a contact. 
- It will first display the contacts in a numbered list and then prompt the user to choose which contact to delete. 
- If the user gives a number out of range or a string, it will alert the user and bring them back to the main menu. 
- It will then delete the contact from the list and notify the user

## 4. Search for a Contact
- This option will allow the user to search for a contact. 
- It will first prompt the user for the name (not case-sensitive) to search for.
- If the name is found in the contact list, it will display the contact's name, phone number, email address, address, and notes. 

## 5. Display All Contacts
- This option will display all the contacts in a numbered list. 

## 6. Export Contacts to a Text File 
- This option will allow the user to export the contacts in the system to a text file, given a file path (of where to save the file) and the file name. 
- It will first prompt the user for the file path and file name.
- If the file path is invalid, it will alert the user. 
- If the file name already exists, it will overwrite the information in the file. 
- The format in the text file will be as follows on each line: 
    name:phone_number,email_address,address,notes
- For any additional errors, the user will be notified and brought back to main menu.

## 7. Import Contacts from a Text File
- This option will allow the user to import contacts from a text file and put them into the current contact list, given a file name path (where to import from). 
- It will first prompt the user for the file name path. 
- If the file name path is invalid, it will alert the user. 
- The format for the text file should be as follows on each line:
    name:phone_number,email_address,address,notes
- For any additional errors, the user will be notified and brought back to main menu. 

## 8. Quit
- This option will thank the user and exit the program.

## Other Things to Note
- The content list is being stored as a dictionary with the following format: 

    {'name': ['phone_number', 'email_address', 'address', 'notes']}  

- I've also provided a text file with some contact information for testing purposes (data.txt).


* This code can be found in this repository:
* https://github.com/ecyates/module-3-mini-project-contact-management-system.git