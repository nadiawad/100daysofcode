name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

score = ""
combined_names = name1.lower() + name2.lower()

digit1 = combined_names.count('t') + combined_names.count('r') + combined_names.count('u') + combined_names.count('e')
digit2 = combined_names.count('l') + combined_names.count('o') + combined_names.count('v') + combined_names.count('e')

score = str(digit1) + str(digit2)
score_as_int = int(score)

if score_as_int < 10 or score_as_int > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score_as_int < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
