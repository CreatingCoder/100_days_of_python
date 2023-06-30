def high_score():
    highest_score = 0
    scores = input('Please input the scores of all the students and separate them by spaces: ').split()

    for score in scores:
        if(int(score) > highest_score):
            highest_score = int(score)

    print(f'The highest score in the class is: {highest_score}')

high_score()
