print("Welcome to the tip calculator! ")
total_bill = float(input ("What was the total bill? "))
tip = int(input("What percentage tip would you like to add? for example(10, 15, 20) "))
people = int(input("How many people are splitting the bill? "))

bill_with_tip = tip / 100 * total_bill + total_bill
print(f"the total bill is  {bill_with_tip}")

indivisual_bill_amt = bill_with_tip / people
individual_pay = round(indivisual_bill_amt, 2)
print(f"Each person should pay : {individual_pay}")



