# palindrome.py 6/13/18

def palindrome(word):
    i = 0
    while i < len(word) // 2:
        if word[i] != word[(i + 1) * -1]:
            print(f"'{word}' is not a palindrome.")
            return
        i += 1
    print(f"'{word}' is a palindrome.")

print("Hello! This is a palindrome tester.")
user_input = input("Please type in a word.\n> ")
palindrome(user_input)
