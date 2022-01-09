# String
print(len("Hello"))
print(len("123"))
print(len(str(123)))
print("Nadi"[0])
print("Nadi"[-1])

# Integer
print("123" + "456")
print(123 + 456)
print(1_000_000)  # 1,000,000

# Float
print(3.1415)

#Boolean
print(True)
print(False)
print(5 > 4)
print(5 < 4)

print(type(5))
print(type("Hi"))
print(type(True))
x = 5.6
print(type(x))
x = str(x)
print(type(x))

two_digit_number = input("Enter a two digit number: ")
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
sum_of_2_digits = first_digit + second_digit
print(sum_of_2_digits)

print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)

weight = input("Enter your weight in kg: ")
height = input("Enter your height in m: ")
bmi = float(weight) / (float(height) ** 2)
print(int(bmi))

print(8 / 3)
print(round(8 / 3))
print(round(8 / 3, 2))
print(int(8 / 3))
print(8 // 3)

result = 4 / 2
result /= 2
print(result)

score = 2
height = 1.8
isWinner = True
#f-string:
print(f"Your score is {score}, your height is {height}, your winning status is {isWinner}")

age = input("What is your current age?")
LIVE_UNTIL = 90
age_as_int = int(age)
years = LIVE_UNTIL - age_as_int
months = years * 12
weeks = years * 52
days = years * 365
print(f"If you live until you are {LIVE_UNTIL}, you have {days} days, {weeks} weeks, and {months} months left.")
