# anagram.py 6/13/18

def check_anagram(str1, str2):
    str1_mod = str1.lower().replace(' ', '') # create string with no spaces
    str2_mod = str2.lower().replace(' ', '')
    str1_list = list(str1_mod) # convert string to list
    str2_list = list(str2_mod)
    str1_list.sort() # sort the list
    str2_list.sort()
    print("This is str1_list: " + str(str1_list))
    print("This is str2_list: " + str(str2_list))
    if str1_list == str2_list:
        print(f"'{str1}' and '{str2}' are anagrams of each other.")
    else:
        print(f"'{str1}' and '{str2}' are not anagrams of each other.")


print("Hello. We are going to see if two words are anagrams.")
string1 = input("Please type in the first word.\n> ")
string2 = input("Please type in the second word.\n> ")
check_anagram(string1, string2)
