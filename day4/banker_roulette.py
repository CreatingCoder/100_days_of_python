import random

def banker_roulette():

    print('Welcome to Banker Roulette - who will pay the bill?')

    person_list = input('Please enter a list of names with each separated by a comma: ')

    person_list = person_list.split()

    rand_choice = random.choice(person_list)

    return print(f'it looks like {rand_choice} will be paying the bill')

banker_roulette()
