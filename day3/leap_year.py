def leap_year():
    userInput = int(input('Which year do you want me to check? '))

    if(userInput%4 == 0):
        if(userInput%100 != 0 or userInput%400 ==0):
            print('Leap Year')
        
    else:
        print('Not Leap Year')

leap_year()
