import random

def blackjack():
    play = True
    hit_me = 'y'

    while play == True:
        user_card= [None] * 21
        cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        user_play = input('Do you want to play a round of blackjack? (y or n): ').lower()
        if user_play == 'n':
            break
        
        # user_card[1] = random.choice(cards)
        # user_card[2] = random.choice(cards)
        for i in range(0, 21):
            user_card[i] = random.choice(cards)
        
        show_comp1 = random.choice(cards)
        hide_comp2 = random.choice(cards)
        
        print(f'Your cards are: [{user_card[1]}, {user_card[2]}]')
        print(f"The computer's first card is {show_comp1}")

        
        pos = 3
        while(hit_me == 'y'):
            user_card[pos] = random.choice(cards)
            hit_me = input("Type 'y' to get another card, or 'n' to pass: ").lower()
            pos = pos + 1
            print(user_card[pos])

            

        
        
def total(a,b):
    """returns total of two variables"""
    return a+b



    
    
    
blackjack()
