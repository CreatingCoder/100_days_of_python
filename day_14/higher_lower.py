import game_data
import random

def higher_lower():
    quest = False
  
    #List with dictionary -> keys are 'name', 'follower_count', 'description', 'country'
    game_list = game_data.data

  
    #This part got a little yucky, 
    run = True
    while run == True:
        if(quest == False):
            rand_a = get_random_int()    
        
        rand_b = get_random_int()

        intro(game_list, rand_a, rand_b)

        quest = question(game_list, rand_a, rand_b)

        if quest == True:
            continue

        else:
            break

    print('You lost')

def get_random_int():
    return random.randint(0, 49)

def intro(list ,rand_intA, rand_intB):
    print(f"Compare A : {list[rand_intA]['name']} , {list[rand_intA]['description']} from {list[rand_intA]['country']}")
    print('VS')
    print(f"Compare B : {list[rand_intB]['name']} , {list[rand_intB]['description']} from {list[rand_intB]['country']}")


def question(g_list, int_a, int_b):
    user_guess = input("Who has more followers?  Type 'A' or 'B'").upper()
    right = True

    # if user guesses A and is correct
    if(user_guess == 'A' and g_list[int_a]['follower_count'] > g_list[int_b]['follower_count']):
        print("Correct! \n")
    
    # if user guesses b and is correct
    elif(user_guess == 'B' and g_list[int_a]['follower_count'] < g_list[int_b]['follower_count']):
        print('Correct! \n')

    # if they have the same amount of followers
    elif(g_list[int_a]['follower_count'] == g_list[int_b]['follower_count']):
        print('They have the same amount of followers!')

    # all other answers are wrong
    else:
        print('Wrong!')
        right = False
    
    return right



higher_lower()
