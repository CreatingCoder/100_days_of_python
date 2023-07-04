def hangman():
    num_guess = 6
    word_to_guess = 'ardvark'
    list_of_guessed_letters = []

    while num_guess > 0:

        guessed_letter = input('Please guess a letter: ')
        list_of_guessed_letters.append(guessed_letter)

        if(guessed_letter not in word_to_guess):
            num_guess = num_guess - 1
        
        output = hangman_output(word_to_guess,  list_of_guessed_letters)

        if('_' not in output):
            print('You won!')
            break

        if(num_guess == 6):
            hangman_none()

        elif(num_guess == 5):
            hangman_one()

        elif(num_guess == 4):
            hangman_two()

        elif(num_guess == 3):
            hangman_three()

        elif(num_guess == 2):
            hangman_four()

        elif(num_guess == 1):
            hangman_five()
       
        elif(num_guess == 0):
           hangman_six()
           print(f'You lost! The word was {word_to_guess}')
           break

        print(output)
    



def hangman_output(w2g, logl):
    output = ''

    for i in w2g:

        if(i in logl):
            output = output + i
        else:
            output = output + '_'


    return output

def hangman_none():
    print('\n _______')
    print('|       |')
    print('|       ')
    print('|')
    print('|')
    print('|')
    print('|')
    print('|')
    print('____________')


def hangman_one():
    print('\n _______')
    print('|       |')
    print('|       O')
    print('|')
    print('|')
    print('|')
    print('|')
    print('|')
    print('____________')

def hangman_two():
    print('\n _______')
    print('|       |')
    print('|       O')
    print('|       |')
    print('|')
    print('|')
    print('|')
    print('|')
    print('____________')

def hangman_three():
    print('\n _______')
    print('|       |')
    print('|       O')
    print('|      /|')
    print('|')
    print('|')
    print('|')
    print('|')
    print('____________')

def hangman_four():
    print('\n _______')
    print('|       |')
    print('|       O')
    print('|      /|\\')
    print('|')
    print('|')
    print('|')
    print('|')
    print('____________')

def hangman_five():
    print('\n _______')
    print('|       |')
    print('|       O')
    print('|      /|\\')
    print('|      /')
    print('|')
    print('|')
    print('|')
    print('____________')

def hangman_six():
    print('\n _______')
    print('|       |')
    print('|       O')
    print('|      /|\\')
    print('|      / \\')
    print('|')
    print('|')
    print('|')
    print('____________')

hangman()




