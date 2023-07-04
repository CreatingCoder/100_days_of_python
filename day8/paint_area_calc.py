def paint_area_calc(height, width, coverage):
    # number of cans = (wall height x wall width) / coverage per can.
    return print(round((height * width) / coverage))

paint_area_calc(height = 2, width=4, coverage=5)
