import os

def calc():
    run = True
    
    
    while run == True:
        
        result = 0
        first_num = float(input('\n\nPlease enter the first number: '))
        user_math = input('Please enter the desired operation ( + - / *): ')
        second_num = float(input('Please enter the second number: '))
        
        if user_math == '+' :
            result = add(first_num, second_num)
            
        elif user_math == '-' :
            result = subtract(first_num, second_num)
            
        elif user_math == '/' :
            result = divide(first_num, second_num)
            
        elif user_math == '*' :
            result = multiply(first_num, second_num)
            
        else:
            print('Wrong input')
            break
            
        print(f'\nThe answer to the equation: {first_num} {user_math} {second_num} = {result}')
        
        run_again = input('\nDo you want to run the program again? (y or n):').lower()
        
        if(run_again == 'n'):
            break
        
        else:
            #clears the screen for the next user
            #os.system('clear')
            continue
            
    
    
    
    
    
    
def add(a, b):
    return a+b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a/b

def multiply(a,b):
    return a * b


calc()
