print("Welcome to my Rollercoaster!")
height = int(input("Enter your height in cm: "))

if height >= 120:
    print("You can play, YAY!")
    age = int(input("How old are you?"))
    if age < 12:
        print("Your ticket is $4.")
    elif age <= 18:
        print("Your ticket is $6")
    else:
        print("Your ticket is $10.")
else:
    print("Sorry :( You cannot play!")


number = int(input("Enter a number to check if it is even or odd?"))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")





height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / (height ** 2))
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi >= 35:
    print(f"Your BMI is {bmi}, you are clinically obese.")

