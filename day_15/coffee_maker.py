import coffee_dict
import os

def coffee_maker():
    user_total = 0.00
    re_dict = coffee_dict.resources
    menu_dict = coffee_dict.MENU
    run = True


    while (run):
        
        userinput = input('What would you like?  Please enter: (espresso, latte, or cappucino): ').lower()
        

        # maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine
        if(userinput == 'off'):
            os.system('cls')
            break

        if(userinput == 'report'):
            print(f"Water: {re_dict['water']}ml")
            print(f"Milk: {re_dict['milk']}ml")
            print(f"Coffee: {re_dict['coffee']}g")
            print(f"Coffee: ${re_dict['money']}")


        if(userinput == 'espresso'):
            dict = make_espresso(re_dict, menu_dict, userinput)

        if(userinput == 'latte'):
            dict = make_latte(re_dict, menu_dict, userinput)
        
        if(userinput == 'cappuccino'):
            dict = make_cappuccino(re_dict, menu_dict, userinput)


def make_espresso(edict, mdict, user_order):

    #if there are enough resources in the coffee maker
    if(edict['water'] >= 50 and edict['coffee'] >= 18):
        print('There are enough resources')
        user_total= money()
        
        #if the user paid enough money
        if(user_total >= mdict['espresso']['cost']):
            edict['water'] = edict['water'] - 50
            edict['coffee'] = edict['coffee'] - 18
            print('Espresso made')

            #return change
            return_change = change(user_total, user_order, mdict)
            print(f'your change is {return_change}')
            
        else:
            print('Sorry, not enough money was provided')

    elif(edict['water'] < 50):
        print('Sorry, there is not enough water')
    elif(edict['coffee'] < 18):
        print('Sorry, there is not enough coffee')



def make_latte(edict, mdict, user_order):

    #if there are enough resources in the coffee maker
    if(edict['water'] >= 200 and edict['coffee'] >= 24 and edict['milk'] >= 150):
        print('There are enough resources')
        user_total= money()
        
        #if the user paid enough money
        if(user_total >= mdict['latte']['cost']):
            edict['water'] = edict['water'] - 200
            edict['coffee'] = edict['coffee'] - 24
            edict['milk'] = edict['milk'] - 150
            print('Latte made')

            #return change
            return_change = change(user_total, user_order, mdict)
            print(f'your change is {return_change}')
            
        else:
            print('Sorry, not enough money was provided')

    elif(edict['water'] < 50):
        print('Sorry, there is not enough water')
    elif(edict['coffee'] < 18):
        print('Sorry, there is not enough coffee')
    elif(edict['milk'] < 150):
        print('Sorry, there is not enough coffee')




def make_cappuccino(edict, mdict, user_order):

    #if there are enough resources in the coffee maker
    if(edict['water'] >= 250 and edict['coffee'] >= 24 and edict['milk'] >= 100):
        print('There are enough resources')
        user_total= money()
        
        #if the user paid enough money
        if(user_total >= mdict['latte']['cost']):
            edict['water'] = edict['water'] - 250
            edict['coffee'] = edict['coffee'] - 24
            edict['milk'] = edict['milk'] - 100
            print('Cappuccino made')

            #return change
            return_change = change(user_total, user_order, mdict)
            print(f'your change is {return_change}')
            
        else:
            print('Sorry, not enough money was provided')

    elif(edict['water'] < 250):
        print('Sorry, there is not enough water')
    elif(edict['coffee'] < 24):
        print('Sorry, there is not enough coffee')
    elif(edict['milk'] < 100):
        print('Sorry, there is not enough coffee')


def money():

    quarters = int(input('How many quarters?  ')) * .25
    dimes = int(input('How many dimes?  ')) * .10
    nickles = int(input('How many nickles?  ')) * .05
    pennies = int(input('How many pennies?  ')) * .01

    return quarters + dimes + nickles + pennies


def change(money_given, order, cost_dict):

    output = 0.0
    print(f'Money given is {round(money_given,2)}')

    if order == 'espresso':
        output = money_given - cost_dict['espresso']['cost']

    if order == 'latte':
        output = money_given - cost_dict['latte']['cost']

    if order == 'cappuccino':
        output = money_given - cost_dict['cappuccino']['cost']

    return round(output,2 )


coffee_maker()

    
