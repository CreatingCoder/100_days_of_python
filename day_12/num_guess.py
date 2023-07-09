import random

def num_guess():

    rand_int = get_rand_num()

    print("\nWelcome to the number guessing game!")
    still_play = input("Please enter 'quit' if you don't want to play, or press enter to continue: ").lower()
    
    if still_play == 'quit':
        quit()
    

    print("\nI'm thinking of a number between 1 and 100")
    difficulty = input("Please choose a difficulty level.  Type 'easy' or 'hard' \n").lower()
    
    if(difficulty == 'easy'):
        easy(rand_int)

    if(difficulty == 'hard'):
        hard(rand_int)



def easy(right_num_easy):
    guesses_easy = 10
    while guesses_easy > 0:
        print(f'You have {guesses_easy} attempts left to guess the number')
        easy_guess = int(input('make a guess: '))
        
        if(easy_guess > right_num_easy):
            print('Too high')
            guesses_easy = guesses_easy - 1

        elif(easy_guess < right_num_easy):
            print('Too low')
            guesses_easy = guesses_easy - 1
        
        elif(easy_guess == right_num_easy):
            print('You won!\n')
            break

    if guesses_easy == 0:
        print('You lost')

    num_guess()
    return None

def hard(right_num_hard):
    guesses_hard = 5
    while guesses_hard > 0:
        print(f'You have {guesses_hard} attempts left to guess the number')
        hard_guess = int(input('make a guess: '))
        
        if(hard_guess > right_num_hard):
            print('Too high')
            guesses_hard = guesses_hard - 1

        elif(hard_guess < right_num_hard):
            print('Too low')
            guesses_hard = guesses_hard - 1
        
        elif(hard_guess == right_num_hard):
            print('You won!\n')
            break

    if guesses_hard == 0:
        print('You lost')

    num_guess()
    return None

def get_rand_num():
    return random.randint(1,100)

num_guess()
