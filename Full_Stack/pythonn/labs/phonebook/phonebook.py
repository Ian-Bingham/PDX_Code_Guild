# phonebook.py 6/20/18

# initial phonebook
# create a dictionary for each contact and put it in a list
phonebook = [
                {"name": "Roxas Amber", "number": "1112223333"},
                {"name": "Axel Blue",  "number": "4445556666"},
                {"name": "Xion Crane", "number": "7778889999"}
            ]


# creates a contact and puts it in the phonebook
def create_contact():
    name = input("Enter the first and last name: ").title()

    # check if the contact already exists. if so, return
    for contact in phonebook:
        if name.lower() in contact["name"].lower():
                print("That contact already exists.")
                return

    # else get the phone number, create the contact,
    # and add them to the phonebook
    number = input("Enter an all digit phone number: ")
    phonebook.append({"name": name, "number": number})
    print("Phonebook has been updated.")


# get contact information
def retrieve_contact():
    name = input("Enter the first and last name: ").title()

    # print the name and number if the person exists in the phonebook
    for contact in phonebook:
        if name.lower() in contact["name"].lower():
                print("{} {}".format(contact["name"], contact["number"]))
                return

    # else, tell the user the contact doesnt exist
    print("That contact does not exist.")


# update contact info
def update_contact():
    name = input("Enter the first and last name of the contact "
                 "you want to update: ").title()

    # check to see if the contact exists
    # if they exist, update their name/number
    for contact in phonebook:
        if name.lower() in contact["name"].lower():
            newName = input("Enter the new name for the contact: ").title()
            newNumber = input("Enter the new number for the contact: ")
            contact["name"] = newName
            contact["number"] = newNumber
            print("Phonebook has been updated.")
            return

    # else, say the contact doesnt exist
    print("That contact does not exist.")


# delete contact from phonebook
def delete_contact():
    name = input("Enter the first and last name of the contact "
                 "you want to delete: ").title()

    # keep track of the index in the phonebook list
    # if we find the name then delete that entry
    i = 0
    for contact in phonebook:
        if name.lower() in contact["name"].lower():
            del phonebook[i]
            print("Phonebook has been updated.")
            return

        i += 1

    # else say the contact doesnt exist
    print("That contact does not exist.")


# display contact information
def show_contact():
    # go through the entire phonebook and display contact info
    for contact in phonebook:
        print("{} {}".format(contact['name'], contact['number']))


# have the user select an option and run the correct functions
def main():
    while True:
        print()
        option = input("Select a contact option: (C)reate, (R)etrieve, "
                       "(U)pdate, (D)elete, (S)how (type done to quit): ")

        print('*' * 50)
        if option.lower() in ["c", "create"]:
            create_contact()
        elif option.lower() in ["r", "retrieve"]:
            retrieve_contact()
        elif option.lower() in ["u", "update"]:
            update_contact()
        elif option.lower() in ["d", "delete"]:
            delete_contact()
        elif option.lower() in ["s", "show"]:
            show_contact()
        elif option.lower() == 'done':
            print("Goodbye!")
            exit(0)
        else:
            print("Not a valid option.")

main()
