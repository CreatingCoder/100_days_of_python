def tips_calc():
    print('Welcome to the tip calculator.')
    bill = float(input('What was the total bill?'))
    percent = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
    people = int(input('How many people to split the bill? '))
    
    tip = (percent/100)* bill
    bill_with_tip = tip + bill
    indiv_bill = bill_with_tip/people
    final_bill = round(indiv_bill, 2) 
    return print(f'Each person should pay: ${final_bill}')

tips_calc()
