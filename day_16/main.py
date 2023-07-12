from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


run = True

while run == True:
    cm = CoffeeMaker()
    menu = Menu()
    
    mm = MoneyMachine()

    userinput = input(f'What would you like?  {menu.get_items()}: ').lower()

    

    if(userinput == 'off'):
        exit()

    if(userinput == 'report'):
        cm.report()

    drink_order = menu.find_drink(userinput)
    

    


    if cm.is_resource_sufficient(drink_order) == True:
        #print(menu_item.cost)
        print
        #get cost of drink
        

        #mm.make_payment()


        

    
