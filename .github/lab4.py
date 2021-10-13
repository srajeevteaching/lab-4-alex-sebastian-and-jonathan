# Programmers: Jonathan, Alex, Sebastian
# Course: CS151, Dr. Rajeev
# Date: Thu Oct 7
# Lab: 4
# Program Inputs: Subscription package and Data usage
# Program Outputs: How much customer owes
import math

subscription_package = input("What is your monthly subscription package? ").strip().lower()
data_usage = int(input("How much data was used? ").strip())

if subscription_package == "green" and data_usage >= 0:
    coupon = input("Do you have coupon? ").strip().lower()
    if coupon == "no":
        if data_usage <= 2:
            monthly_rate = 49.99
        if data_usage >= 2:
            additional_gb = 14.99
            difference_needed = data_usage - 2
            total_extra = additional_gb * difference_needed
            monthly_rate = round(49.99 + total_extra, 2)
    if coupon == "yes":
        if data_usage <= 2:
            monthly_rate = 49.99
        if data_usage >= 2:
            additional_gb = 14.99
            difference_needed = data_usage - 2
            total_extra = additional_gb * difference_needed
            monthly_rate = round(49.99 + total_extra, 2)
            if monthly_rate >= 75:
                monthly_rate = monthly_rate - 20
elif subscription_package == "orange" and data_usage >= 0:
    if data_usage <= 4:
        monthly_rate = 69.99
    if data_usage >= 4:
        additional_gb = 9.99
        difference_needed = data_usage - 4
        total_extra = additional_gb * difference_needed
        monthly_rate = round(69.99 + total_extra, 2)
elif subscription_package == "purple" and data_usage >= 0:
    monthly_rate = 99.99
elif data_usage < 0:
    print("Data used is invalid!")
else:
    print("subscription package is invalid !")

print("Your total owed is: " + str(monthly_rate))
