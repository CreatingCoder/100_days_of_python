import random

def coinflip():
    
    coin = random.randint(0,1)

    if(coin == 0):
        print('Head')

    else:
        print('Tail')

coinflip()
