def avg_height():
    total_weight = 0

    height_list = input('Please input a list of heights separated by a space: ').split()

    for height in height_list:
        total_weight = total_weight + int(height)

    print(f'The average height is {int(total_weight/len(height_list))}')

avg_height()
