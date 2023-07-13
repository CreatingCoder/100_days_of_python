from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


run = True

cm = CoffeeMaker()
menu = Menu()
mm = MoneyMachine()

while run == True:

    userinput = input(f'What would you like?  {menu.get_items()}: ').lower()


    if(userinput == 'off'):
        exit()

    if(userinput == 'report'):
        cm.report()

    drink_order = menu.find_drink(userinput)
    

    if cm.is_resource_sufficient(drink_order) == True and mm.make_payment(drink_order.cost):
        cm.make_coffee(drink_order)

    


        

    
