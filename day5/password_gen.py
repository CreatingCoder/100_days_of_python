import random

def password_gen():
    final_string = ''
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    input_letters = int(input("How many letters would you like in your password?\n")) 
    input_symbols = int(input(f"How many symbols would you like?\n"))
    input_numbers = int(input(f"How many numbers would you like?\n"))
    print('\n')

    lists_combined = [letters, numbers, symbols]

    while input_letters > 0:
        input_letters = input_letters -1
        final_string = final_string + letters[random.randint(0, len(letters)-1)]

    while input_numbers > 0:
        input_numbers = input_numbers -1
        final_string = final_string + numbers[random.randint(0, len(numbers)-1)]

    while input_symbols > 0:
        input_symbols = input_symbols -1
        final_string = final_string + symbols[random.randint(0, len(symbols)-1)]

        final_string = ''.join(random.sample(final_string,len(final_string)))

    print(f'Your randomized password is: {final_string}')

password_gen()
