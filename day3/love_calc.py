def love_calc():

    STR1 = 'true'
    STR2 = 'love'
    score1 = 0 
    score2 = 0

    
    print('Welcome to the Love Calculator!')
    name1 = input('What is your name? \n').lower()
    name2 = input('What is their name? \n').lower()
    
    for i in name1:
        if(i in STR1):
            score1 = score1 + 1
    
    for i in name2:
        if(i in STR1):
            score1 = score1 + 1
            
    for i in name1:
        if(i in STR2):
            score2 = score2 + 1

    for i in name2:
        if(i in STR2):
            score2 = score2 + 1         

    final_score = str(score1) + str(score2)
    final_score = int(final_score)

    if(final_score < 10 or final_score > 90):
        return print(f'Your score is {final_score}, you go together like coke and mentos.')
    
    elif(final_score >= 40 and final_score <= 50):
        return print(f'Your score is {final_score}, you are alright together')

    else:
        return print(f'Your score is {final_score}')
        
love_calc()
