print("Welcome to my Rollercoaster!")
height = int(input("Enter your height in cm: "))
bill = 0

if height >= 120:
    print("You can play, YAY!")
    age = int(input("How old are you?"))
    if age < 12:
        bill = 4
        print("Child ticket is $4.")
    elif age <= 18:
        bill = 6
        print("Youth ticket is $6")
    else:
        bill = 10
        print("Adult ticket is $10.")
    wants_photo = input("Do you want a photo taken? Y/N. ")
    if wants_photo == "Y":
        bill += 4
        print("This will be an extra $4!")
    else:
        print("Ok! No photos will be taken!")
    print(f"Your total bill is: {bill}")
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


print("Welcome to Nadi's Pizza Shop!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")