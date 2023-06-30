def even_num_add():

    total = 0
    for even_num in range(0, 101, 2):
        total = total + even_num

    return print(f'{total}')

even_num_add()
