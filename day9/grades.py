#Dict practice

student_scores = {
    "Harry" : 81, 
    "Hermione" : 99, 
    "Ron" : 78,
    "Draco" : 74, 
    "Neville" : 63
}

student_grades = student_scores.copy()

for key in student_grades:
    if(student_grades[key] <= 100 and student_grades[key] > 90):
        student_grades[key] = 'Outstanding'

    elif(student_grades[key] <= 90 and student_grades[key] > 80):
        student_grades[key] = 'Exceeded Expectations'

    elif(student_grades[key] <= 80 and student_grades[key] > 70):
        student_grades[key] = 'Satisfactory'

    elif(student_grades[key] <= 70):
        student_grades[key] = 'Failed'

print(student_grades)
