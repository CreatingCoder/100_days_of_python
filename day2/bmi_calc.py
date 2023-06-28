def BMICalc():
    weight = float(input('Please input your weight(lb): '))
    height = float(input('Please input your height (inches):'))
    
    if(weight is str):
        print('Error: You did not enter a number')
    
    bmi = str(round(weight/(height**2)*703))
    
    return print('Your BMI is ' + bmi)
    
BMICalc()
        
