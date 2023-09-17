#range(1,5) -> result should be 2,4,6,8
# list = [ n*2 for n in range(1,5)]
# print(list)
#----------------------------------------------
# names = ['Bob', 'asdfas', 'Alex', 'FGHFGH']
# short_names = [name for name in names if len(name) <=4]
# print(short_names)
#-----------------------------------
#numbers = [1,1,2,3,5,8,13,21,34,55]
#squared = [n*n  for n in numbers]
#print(squared)
#-------------------------------
# numbers = [1,1,2,3,5,8,13,21,34,55]
# even_numbers = [n for n in numbers if n%2 ==0]
# print(even_numbers)
#----------------------------------

# with open('file1.txt') as file1:
#     f1_list = [int(f1.strip()) for f1 in file1]

# with open('file2.txt') as file2:
#     f2_list = [int(f2.strip())for f2 in file2]

# num_in_both = [int(num)for num in f1_list if num in f2_list]
# print(num_in_both) 

#-----Dict------------------------------------
# import random as rand
# students = [
#     'Jones',
#     'Matt', 
#     'John', 
#     'Sean' 
# ]

# stud_scores = {student:rand.randint(1,100) for student in students}
# print(stud_scores)

# passed = {student:score for (student,score) in stud_scores.items() if score>=60}
# print(passed)
#--------------------------------------------------------------------------------
# string = 'what is the airspeed velocity of an unladen swallow?'
# dict = {thing:len(thing) for thing in string.split()}
# print(dict)
#--------------------------------------------------------------------------------
weather_c = {
    'Monday' : 12,
    'Tuesday' : 14,
    'Wednesday' : 15,
    'Thursday' : 14,
    'Friday' : 21,
    'Saturday' : 22,
    'Sunday' : 24
}

#Equation is: C * 9/5 + 32 = Far.
#            m1       m2                  m1    m2        dict  
weather_f = {day:(temp_c*9/5) + 32 for (day,temp_c) in weather_c.items()}
print(weather_f)