import random

def blackjack():
    play = True


    while play == True:
        user_card= [None] * 21
        cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        num_cards = 2
        user_play = input('Do you want to play a round of blackjack? (y or n): ').lower()
        
        if user_play == 'n':
            break
    
        for i in range(0, 21):
            user_card[i] = random.choice(cards)
        
        show_comp1 = random.choice(cards)
        hide_comp2 = random.choice(cards)
        
        print(f'Your cards are: [{user_card[1]}, {user_card[2]}]')
        print(f"The computer's first card is {show_comp1}")

        #run(,num_cards)

            

        
        
def total(a,b):
    """returns total of two variables"""
    return a+b

def run(card_count):
    hit_me = input("Type 'y' to get another card, or 'n' to pass: ").lower()
    if(hit_me == 'y'):
        run()
   
    return print('yeet')
    

    
    
    
blackjack()
