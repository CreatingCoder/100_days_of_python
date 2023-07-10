import coffee_dict
import os

def coffee_maker():
    # dict = {
    #     'water' : 300,
    #     'milk' : 200,
    #     'coffee' : 100,
    #     'money' : 0.00
    # }

    dict = coffee_dict.resources

    run = True
    # print(coffee_dict.MENU['espresso'])
    # print(coffee_dict.MENU['espresso']['ingredients'])

    while (run):
        
        userinput = input('What would you like?  Please enter: (espresso, latte, or cappucino): ').lower()

        # maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine
        if(userinput == 'off'):
            os.system('cls')
            break

        if(userinput == 'report'):
            print(f"Water: {dict['water']}ml")
            print(f"Milk: {dict['milk']}ml")
            print(f"Coffee: {dict['coffee']}g")
            print(f"Coffee: ${dict['money']}")


        if(userinput == 'espresso'):
            dict = make_espresso(dict)
            #print(dict)





def make_espresso(edict):

    if(edict['water'] >= 50 and edict['coffee'] >= 18):
        print('There are enough resources')
        money()
        
        # edict['water'] = edict['water'] - 50
        # edict['coffee'] = edict['coffee'] - 18



    elif(edict['water'] < 50):
        print('Sorry, there is not enough water')
    elif(edict['coffee'] < 18):
        print('Sorry, there is not enough coffee')




        
    


def money():
    quarters = int(input('How many quarters?  '))
    dimes = int(input('How many dimes?  '))
    nickles = int(input('How many nickles?  '))
    pennies = int(input('How many pennies?  '))









coffee_maker()

    
