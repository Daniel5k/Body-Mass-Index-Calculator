#BMI = (weight in pounds x 703)/(height in inches x height in inches)
#we will have two inputs and a constant of 703
#we will have a function that takes in two parameters
#a loop to continue the calculation for another person

constantValue = 703
def gettingInputs():
    weight = int(input('Enter your weight in pounds: \n'))
    HeightInches = int(input('Enter your height in inches: \n'))
    HeightInch = int(input('Enter Another height in inches: \n'))
    result = (weight*constantValue)/(HeightInches*HeightInch)
    print(f'Your BMI is: {result}')

while True:
    gettingInputs()
    progress = input('Do you want to continue? y/n\n')
    if progress == "y" or "Y":
        gettingInputs()
    else:
        break
