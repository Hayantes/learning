def is_palindrome(user_input):
    normalized_input = ''.join(char.lower() for char in user_input if char.isalnum())

    if normalized_input == normalized_input[::-1]:
        print(f'"{user_input}" is a palindrome!')
    else:
        print(f'"{user_input}" is not a palindrome.')


user_word = input("Please enter a word or phrase: ")
is_palindrome(user_word)