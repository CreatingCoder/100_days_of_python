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
        
        final_cards = run(num_cards, user_card, show_comp1)

        print(f"the player's final cards are: {final_cards}")

            

        
        
def total(a,b):
    """returns total of two variables"""
    return a+b

def run(card_count, players_cards, comp_shown_card):


    print(f'Your cards are: {players_cards[:card_count]}')
    print(f"The computer's first card is {comp_shown_card}")

    hit_me = input("Type 'y' to get another card, or 'n' to pass: ").lower()
    

    if(hit_me == 'y'):
        #add another card
        card_count = card_count + 1 
        run(card_count, players_cards, comp_shown_card)
    
    elif(hit_me == 'n'):
        return players_cards[:card_count]
    
    #return print('yeet')


        

    

    
    

    
    
    
blackjack()
