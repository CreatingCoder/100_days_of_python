def daysLeft():
    ##Assumption that user will live to 90 years old
    daysTotal = int(90 * 365)
    userAge = int(input('What is your current age? '))
    
    days = round(daysTotal - userAge * 365)
    weeks = round((90- userAge) * 52)
    months = round((90 - userAge) * 12)
    
    return print(f'You have {days}, {weeks} weeks, and {months} months left.')

daysLeft()
