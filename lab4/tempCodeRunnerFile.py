import os
from datetime import datetime

class ContactBook:
    def __init__(self, filename="contacts.txt"):
        self.filename = filename
        self.ensure_file_exists()
    
    def ensure_file_exists(self):
        """Create the contacts file if it doesn't exist"""
        try:
            if not os.path.exists(self.filename):
                with open(self.filename, 'w') as file:
                    file.write("# Contact Book - Format: Name,Phone\n")
                print(f"Created new contact file: {self.filename}")
        except Exception as e:
            print(f"Error creating file: {e}")
    
    def add_contact(self, name, phone):
        """Add a new contact to the file"""
        try:
            # Validate input
            if not name.strip() or not phone.strip():
                print("Error: Name and phone cannot be empty!")
                return False
            
            # Check for duplicate
            if self.contact_exists(name):
                print(f"Contact '{name}' already exists!")
                choice = input("Do you want to update it? (y/n): ").lower()
                if choice == 'y':
                    return self.update_contact(name, phone)
                return False
            
            # Append new contact
            with open(self.filename, 'a') as file:
                file.write(f"{name},{phone}\n")
            
            print(f" Contact '{name}' added successfully!")
            return True
            
        except PermissionError:
            print("Error: Permission denied. Cannot write to contact file.")
            return False
        except Exception as e:
            print(f"Error adding contact: {e}")
            return False
    
    def view_all_contacts(self):
        """Display all contacts from the file"""
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
            
            # Filter out comments and empty lines
            contacts = []
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):
                    contacts.append(line)
            
            if not contacts:
                print(" No contacts found in the contact book.")
                return
            
            print("\n" + "="*50)
            print(" ALL CONTACTS")
            print("="*50)
            print(f"{'No.':<4} {'Name':<20} {'Phone':<15}")
            print("-"*50)
            
            for i, contact in enumerate(contacts, 1):
                try:
                    name, phone = contact.split(',', 1)
                    print(f"{i:<4} {name:<20} {phone:<15}")
                except ValueError:
                    print(f"{i:<4} Invalid format: {contact}")
            
            print("-"*50)
            print(f"Total contacts: {len(contacts)}")
            
        except FileNotFoundError:
            print(f"Error: Contact file '{self.filename}' not found!")
            print("Try adding a contact first.")
        except Exception as e:
            print(f"Error reading contacts: {e}")
    
    def search_contact(self, search_term):
        """Search for contacts by name or phone"""
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
            
            search_term = search_term.lower().strip()
            found_contacts = []
            
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):
                    try:
                        name, phone = line.split(',', 1)
                        if (search_term in name.lower() or 
                            search_term in phone.lower()):
                            found_contacts.append((name, phone))
                    except ValueError:
                        continue
            
            if not found_contacts:
                print(f" No contacts found matching '{search_term}'")
                return
            
            print(f"\n SEARCH RESULTS for '{search_term}'")
            print("="*40)
            print(f"{'Name':<20} {'Phone':<15}")
            print("-"*40)
            
            for name, phone in found_contacts:
                print(f"{name:<20} {phone:<15}")
            
            print("-"*40)
            print(f"Found {len(found_contacts)} contact(s)")
            
        except FileNotFoundError:
            print(f"Error: Contact file '{self.filename}' not found!")
        except Exception as e:
            print(f"Error searching contacts: {e}")
    
    def contact_exists(self, name):
        """Check if a contact already exists"""
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
            
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):
                    try:
                        existing_name, _ = line.split(',', 1)
                        if existing_name.lower() == name.lower():
                            return True
                    except ValueError:
                        continue
            return False
            
        except FileNotFoundError:
            return False
        except Exception:
            return False
    
    def update_contact(self, name, new_phone):
        """Update an existing contact's phone number"""
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
            
            updated = False
            updated_lines = []
            
            for line in lines:
                if line.strip() and not line.startswith('#'):
                    try:
                        existing_name, old_phone = line.strip().split(',', 1)
                        if existing_name.lower() == name.lower():
                            updated_lines.append(f"{existing_name},{new_phone}\n")
                            updated = True
                            print(f" Updated {existing_name}: {old_phone} → {new_phone}")
                        else:
                            updated_lines.append(line)
                    except ValueError:
                        updated_lines.append(line)
                else:
                    updated_lines.append(line)
            
            if updated:
                with open(self.filename, 'w') as file:
                    file.writelines(updated_lines)
                return True
            else:
                print(f"Contact '{name}' not found!")
                return False
                
        except Exception as e:
            print(f"Error updating contact: {e}")
            return False
    
    def delete_contact(self, name):
        """Delete a contact from the file"""
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
            
            deleted = False
            updated_lines = []
            
            for line in lines:
                if line.strip() and not line.startswith('#'):
                    try:
                        existing_name, phone = line.strip().split(',', 1)
                        if existing_name.lower() != name.lower():
                            updated_lines.append(line)
                        else:
                            deleted = True
                            print(f" Deleted contact: {existing_name} ({phone})")
                    except ValueError:
                        updated_lines.append(line)
                else:
                    updated_lines.append(line)
            
            if deleted:
                with open(self.filename, 'w') as file:
                    file.writelines(updated_lines)
                return True
            else:
                print(f"Contact '{name}' not found!")
                return False
                
        except Exception as e:
            print(f"Error deleting contact: {e}")
            return False
    
    def export_contacts(self, export_file="contacts_backup.txt"):
        """Export all contacts to a backup file"""
        try:
            with open(self.filename, 'r') as source:
                content = source.read()
            
            with open(export_file, 'w') as backup:
                backup.write(f"# Contact Book Backup - {datetime.now()}\n")
                backup.write(content)
            
            print(f" Contacts exported to '{export_file}'")
            
        except Exception as e:
            print(f"Error exporting contacts: {e}")

def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print(" CLI CONTACT BOOK")
    print("="*50)
    print("1. Add new contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Export contacts")
    print("7. Exit")
    print("-"*50)

def main():
    """Main function to run the contact book CLI"""
    contact_book = ContactBook()
    
    print(" Welcome to CLI Contact Book!")
    print("Your contacts are stored in 'contacts.txt'")
    
    while True:
        try:
            display_menu()
            choice = input("Enter your choice (1-7): ").strip()
            
            if choice == '1':
                print("\n ADD NEW CONTACT")
                name = input("Enter name: ").strip()
                phone = input("Enter phone: ").strip()
                contact_book.add_contact(name, phone)
                
            elif choice == '2':
                contact_book.view_all_contacts()
                
            elif choice == '3':
                print("\n SEARCH CONTACT")
                search_term = input("Enter name or phone to search: ").strip()
                if search_term:
                    contact_book.search_contact(search_term)
                else:
                    print("Search term cannot be empty!")
                    
            elif choice == '4':
                print("\n UPDATE CONTACT")
                name = input("Enter name to update: ").strip()
                if name:
                    new_phone = input("Enter new phone number: ").strip()
                    contact_book.update_contact(name, new_phone)
                else:
                    print("Name cannot be empty!")
                    
            elif choice == '5':
                print("\n DELETE CONTACT")
                name = input("Enter name to delete: ").strip()
                if name:
                    confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ")
                    if confirm.lower() == 'y':
                        contact_book.delete_contact(name)
                else:
                    print("Name cannot be empty!")
                    
            elif choice == '6':
                print("\n EXPORT CONTACTS")
                export_file = input("Enter backup filename (or press Enter for default): ").strip()
                if not export_file:
                    export_file = "contacts_backup.txt"
                contact_book.export_contacts(export_file)
                
            elif choice == '7':
                print("\n Thank you for using CLI Contact Book!")
                print("Your contacts are safely stored in 'contacts.txt'")
                break
                
            else:
                print(" Invalid choice! Please enter 1-7.")
                
        except KeyboardInterrupt:
            print("\n\n Goodbye! Exiting Contact Book...")
            break
        except Exception as e:
            print(f" An unexpected error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()