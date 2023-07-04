import math

def paint_area_calc(height, width, coverage):
    # number of cans = (wall height x wall width) / coverage per can.
    return print(int(math.ceil((height * width) / coverage)))

paint_area_calc(height = 7, width=13, coverage=5)
