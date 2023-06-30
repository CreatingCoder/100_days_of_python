def fizzbuzz():

    for num in range(0,101,1):
        
        if((num % 3) == 0):
            print('fizz')
        elif((num % 5 ) == 0):
            print('buzz')
        else:
            print(num)

fizzbuzz()
