print("Welcome to my Tip Calculator!")
total_bill = float(input("What was the total bill? $"))
selected_tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people_to_pay = int(input("How many people to split the bill? "))
total_bill_plus_tip = total_bill + (total_bill * selected_tip_percentage / 100)
amount_for_each_person_to_pay = total_bill_plus_tip / number_of_people_to_pay
print("Each person should be pay: $", "{:.2f}".format(round(amount_for_each_person_to_pay, 2)))