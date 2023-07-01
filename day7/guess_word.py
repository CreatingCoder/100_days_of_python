import random

def guess_word():

    word_list = ['ardvark', 'baboon', 'camel']
    random_word = random.choice(word_list)
    guess_letter = input('Please guess a letter: ')

    for i in random_word:
        if(i == guess_letter):
            print(guess_letter, end = ' ')
        else:
            print('_', end = ' ')

    

guess_word()
