# phonebook.py 6/20/18

phonebook = [
                {"name": "Roxas Amber", "number": "1112223333"},
                {"name": "Axel Blue",  "number": "4445556666"},
                {"name": "Xion Crane", "number": "7778889999"}
            ]

def create_contact():
    name = input("Enter the first and last name: ").title()

    for contact in phonebook:
        if name.lower() in contact["name"].lower():
                print("That contact already exists.")
                return

    number = input("Enter an all digit phone number: ")
    phonebook.append({"name": name, "number": number})
    print("Phonebook has been updated.")

def retrieve_contact():
    name = input("Enter the first and last name: ").title()

    for contact in phonebook:
        if name.lower() in contact["name"].lower():
                print("{} {}".format(contact["name"], contact["number"]))
                return

    print("That contact does not exist.")

def update_contact():
    name = input("Enter the first and last name of the contact you want to update: ").title()

    for contact in phonebook:
        if name.lower() in contact["name"].lower():
            newName = input("Enter the new name for the contact: ").title()
            newNumber = input("Enter the new number for the contact: ")
            contact["name"] = newName
            contact["number"] = newNumber
            print("Phonebook has been updated.")
            return

    print("That contact does not exist.")

def delete_contact():
    name = input("Enter the first and last name of the contact you want to delete: ").title()

    i = 0
    for contact in phonebook:
        if name.lower() in contact["name"].lower():
            del phonebook[i]
            print("Phonebook has been updated.")
            return

        i += 1

    print("That contact does not exist.")

def show_contact():
    for contact in phonebook:
        print("{} {}".format(contact['name'], contact['number']))

def main():
    while True:
        print()
        contact_option = input("Select a contact option: (C)reate, (R)etrieve, \
(U)pdate, (D)elete, (S)how (type done to quit): ")

        print('*' * 50)
        if contact_option.lower() in ["c", "create"]:
            create_contact()
        elif contact_option.lower() in ["r", "retrieve"]:
            retrieve_contact()
        elif contact_option.lower() in ["u", "update"]:
            update_contact()
        elif contact_option.lower() in ["d", "delete"]:
            delete_contact()
        elif contact_option.lower() in ["s", "show"]:
            show_contact()
        elif contact_option.lower() == 'done':
            print("Goodbye!")
            exit(0)
        else:
            print("Not a valid option.")

main()
