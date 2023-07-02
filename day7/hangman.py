def hangman():

    word = 'ardvark'
    miss_count = 1
    userInput = input('Please guess a letter:')

    for j in range(0,6):
        userInput = input('Please guess a letter:')

        for i in word:

            if(i == userInput):
                print(i,end = "")
            else:
                print('_', end ="")
                      
        print(f'You now have used {miss_count} of your 6 tries')
        miss_count = miss_count + 1
     
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

def hangman_five():
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
