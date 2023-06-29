def pizza_order():
    bill = 0.0
    print('Welcome to Python Pizza Deliveries')
    size = input('What size pizza do you want? S,M, or L? ')
    pep = input('Do you want pepperoni? Y or N?')
    extra_cheese = input('Do you want extra cheese? Y or N?')

    if(size == 'S'):
        bill = 15
    
    elif(size == 'M'):
        bill = 20

    else:
        bill = 25

    if(pep == 'Y' and size == 'S'):
        bill = bill + 2
    
    elif(pep == 'Y' and (size == 'M' or size == 'L')):
        bill = bill + 3

    if(extra_cheese == 'Y'):
        bill = bill + 1
 
    return print(f'Your final bill is ${bill}')

pizza_order()


    
    
    
