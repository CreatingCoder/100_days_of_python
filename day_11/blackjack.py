import random

def blackjack():
    play = True

    while play == True:
        user_card= [None] * 21
        cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        num_cards = 2
        user_play = input('\nDo you want to play a round of blackjack? (y or n): ').lower()
        
        if user_play == 'n':
            break
    
        for i in range(0, 21):
            user_card[i] = random.choice(cards)
        
        show_comp1 = random.choice(cards)
        hide_comp2 = random.choice(cards)
        
        final_cards = run(num_cards, user_card, show_comp1)

        print(f"\nthe player's final cards are: {final_cards}")
        print(f"the computer's final cards are: [{show_comp1}, {hide_comp2}]")
        print(f"\nThe player's total is {sum(final_cards)}")
        print(f"The computer's total is {show_comp1 + hide_comp2}\n")

        if(sum(final_cards) > (show_comp1 + hide_comp2)):
            print('Congrats!  You won!\n')

        elif(sum(final_cards) < (show_comp1 + hide_comp2)):
            print('Sorry, the house won.  Nice try!\n')

        elif(sum(final_cards) == (show_comp1 + hide_comp2)):
            print('Looks like a draw!\n')

def run(card_count, players_cards, comp_shown_card):
    
    print(f'\nYour cards are: {players_cards[:card_count]}')
    print(f"The computer's first card is {comp_shown_card}\n")
    card_count = card_count + 1 
    hit_me = input("Type 'y' to get another card, or 'n' to pass: ").lower()
    

    if(hit_me == 'y'):
        #add another card
        #card_count = card_count + 1 
        run(card_count, players_cards, comp_shown_card)
    
    elif(hit_me == 'n'):
        card_count = card_count - 1

    return players_cards[:card_count]
            
blackjack()
