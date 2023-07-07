import os

def silent_auction():
    run = True
    bidders_dict = {}
    winning_bid = 0
    winner = ''

    while run == True:
        print('Hello, welcome to the Silent Auction.')
        name = input('Please enter your name: ')
        bid = input('Please enter your bid: ')

        bidders_dict[name] = bid

        next = input('Is there anyone else who wants to bid?  Type "yes" or "no": ').lower()

        #if next == 'yes': 
        os.system('clear')

        if next == 'yes':
            continue
        else:
            break
    
    for value in bidders_dict:
        if(int(bidders_dict[value]) > winning_bid):
            winning_bid = int(bidders_dict[value])
            winner = value

    print(f'\n{winner} won the silent auction with a high bid of {winning_bid}!')

silent_auction()
