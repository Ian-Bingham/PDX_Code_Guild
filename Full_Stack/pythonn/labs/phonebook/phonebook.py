# phonebook.py 6/20/18

import csv


# get contents from csv and represent it as a dict of dicts
# {name: {'name': name, 'number': num}, name2: {'name': name2, 'number': num}}
def load_csv():
    phonebook = {}
    with open('phonebook.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            phonebook[row["name"]] = dict(row)
        return phonebook


# write the phonebook into the csv
def write_csv(phonebook):
    with open('phonebook.csv', 'w') as csv_file:
        field_names = ['name', 'number']
        csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
        csv_writer.writeheader()
        for key, val in phonebook.items():
            csv_writer.writerow(val)


# creates a contact and puts it in the phonebook
def create_contact(phonebook):
    name = input("Enter the first and last name: ").title()

    # check if the contact already exists. if so, return
    for key, val in phonebook.items():
        if name.lower() == key.lower():
                print("That contact already exists.")
                return

    # else get the phone number, create the contact,
    # and add them to the phonebook
    number = input("Enter an all digit phone number: ")
    phonebook[name] = {'name': name, 'number': number}
    write_csv(phonebook)
    print("Phonebook has been updated.")


# get contact information
def retrieve_contact(phonebook):
    name = input("Enter the first and last name: ").title()

    # print the name and number if the person exists in the phonebook
    for key, val in phonebook.items():
        if name.lower() == key.lower():
                print("{} {}".format(val["name"], val["number"]))
                return

    # else, tell the user the contact doesnt exist
    print("That contact does not exist.")


# update contact info
def update_contact(phonebook):
    name = input("Enter the first and last name of the contact "
                 "you want to update: ").title()

    # check to see if the contact exists
    # if they exist, update their name/number
    for key, val in phonebook.items():
        if name.lower() == key.lower():
            newName = input("Enter the new name for the contact: ").title()
            newNumber = input("Enter the new number for the contact: ")
            phonebook[name] = {'name': newName, 'number': newNumber}
            write_csv(phonebook)
            print("Phonebook has been updated.")
            return

    # else, say the contact doesnt exist
    print("That contact does not exist.")


# delete contact from phonebook
def delete_contact(phonebook):
    name = input("Enter the first and last name of the contact "
                 "you want to delete: ").title()

    # keep track of the index in the phonebook list
    # if we find the name then delete that entry
    for key, val in phonebook.items():
        if name.lower() == key.lower():
            del phonebook[key]
            write_csv(phonebook)
            print("Phonebook has been updated.")
            return

    # else say the contact doesnt exist
    print("That contact does not exist.")


# display contact information
def show_contact(phonebook):
    # go through the entire phonebook and display contact info
    for key, val in phonebook.items():
        print("{} {}".format(val['name'], val['number']))


# have the user select an option and run the correct functions
def main():
    while True:
        print()
        print("Welcome to Phonebook!")
        phonebook = load_csv()
        # noinspection SpellCheckingInspection
        option = input("Select a contact option: (C)reate, (R)etrieve, "
                       "(U)pdate, (D)elete, (S)how (enter to quit): ")

        print('*' * 50)
        if option.lower() in ["c", "create"]:
            create_contact(phonebook)
        elif option.lower() in ["r", "retrieve"]:
            retrieve_contact(phonebook)
        elif option.lower() in ["u", "update"]:
            update_contact(phonebook)
        elif option.lower() in ["d", "delete"]:
            delete_contact(phonebook)
        elif option.lower() in ["s", "show"]:
            show_contact(phonebook)
        elif not option.lower():
            print("Goodbye!")
            exit(0)
        else:
            print("Not a valid option.")


main()
