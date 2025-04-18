#BMI = (weight in pounds x 703)/(height in inches x height in inches)
#we will have two inputs and a constant of 703
#we will have a function that takes in two parameters
#a loop to continue the calculation for another person

constantValue = 703
def gettingInputs():
    try:
        weight = float(input('Enter your weight in pounds: \n'))
        HeightInches = float(input('Enter your height in inches: \n'))
        HeightInch = float(input('Enter Another height in inches: \n'))
        result = float((weight * constantValue) / (HeightInches * HeightInch))
        print(f'Your BMI is: {result}')
    except ValueError:
        print("Invalid Input")

while True:
    gettingInputs()
    progress = input('Do you want to continue? y/n where y is "yes" and n is "no"\n')
    if progress.lower() == "y" or progress.lower() == "yes":
        continue
    else:
        break


