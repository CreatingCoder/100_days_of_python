def prime_num(number):
    prime = True

    for i in range(2, number):

      if(number % i == 0):
          prime = False
    
    if(prime == True):
        return print(f'The number {number} is a prime number')

    if(prime == False):
        return print(f'The number {number} is NOT a prime number')
    
prime_num(38)
