##BMI Calc 2.0
def BMICalc():
    weight = float(input('Please input your weight(lb): '))
    height = float(input('Please input your height (inches):'))
    diag = ''
    
    if(weight is str):
        print('Error: You did not enter a number')
    
    bmi =round(weight/(height**2)*703)
    
    if(bmi < 18.5):
        diag = 'underweight'

    elif(bmi > 18.5 and bmi <= 25):
        diag = 'normal weight'

    elif(bmi > 25 and bmi <= 30):
        diag = 'overweight'

    elif(bmi > 30 and bmi <= 35):
        diag = 'obese'

    elif(bmi > 35 ):
        diag = 'clinically obese'

    return print(f'Your BMI is {bmi} and you are {diag}' )

BMICalc()
        
