fname= 'john'
lname = 'DoE'

def format_name(fname, lname):
    fname = fname.title()
    lname = lname.title()
    return fname + " " + lname

yeet =format_name(fname, lname)
print(yeet)
