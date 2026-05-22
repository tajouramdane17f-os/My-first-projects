#====================================================================================
# project: currency converter
# description: this program converts an amount of money from one currency to another
# date created: 2026-05-22
#====================================================================================

# welcome message and instructions
print ("hello in currency converter")
print("available currency: USD, EUR, GBP, DZD")
amount = float(input("enter the amount you want to convert: "))
print("the amount you want to convert is: " + str(amount))
from_currency = input("enter currency you want to convert from: ")
to_currency = input("enter currency you want to convert to: ")
#=======================================================================
# conversion rates (changind over time, so you may want to update them)
#=======================================================================
# USD --> EUR
if from_currency == "USD" and to_currency == "EUR" :
    converted_amount = amount * 0.85
    print(str(amount) + " " + from_currency + " is equal to " + str(converted_amount) + " " + to_currency)
# EUR --> USD
elif from_currency == "EUR" and to_currency == "USD" :
    converted_amount = amount / 0.85
    print(str(amount) + " " + from_currency + " is equal to " + str(converted_amount) + " " + to_currency)
# USD --> GBP
elif from_currency == "USD" and to_currency == "GBP" :
    converted_amount = amount / 1.3 
    print(str(amount) + " " + from_currency + " is equal to " + str(converted_amount) + " " + to_currency)
# GBP --> USD
elif from_currency == "GBP" and to_currency == "USD" :
    converted_amount = amount *1.3 
    print(str(amount) + " " + from_currency + " is equal to " + str(converted_amount) + " " + to_currency)
# USD --> DZD
elif from_currency == "USD" and to_currency == "DZD" :
    converted_amount = amount * 135.5
    print(str(amount) + " " + from_currency + " is equal to " + str(converted_amount) + " " + to_currency)
# DZD --> USD
elif from_currency == "DZD" and to_currency == "USD" :
    converted_amount = amount / 135.5
    print(str(amount) + " " + from_currency + " is equal to " + str(converted_amount) + " " + to_currency)
# EUR --> GBP
elif from_currency == "EUR" and to_currency == "GBP" :
    converted_amount = amount * 1.15
    print(str(amount) + " " + from_currency + " is equal to " + str(converted_amount) + " " + to_currency)
# GBP --> EUR
elif from_currency == "GBP" and to_currency == "EUR" :
    converted_amount = amount / 1.15
    print(str(amount) + " " + from_currency + " is equal to " + str(converted_amount) + " " + to_currency)
# EUR --> DZD
elif from_currency == "EUR" and to_currency == "DZD" :
    converted_amount = amount * 270
    print(str(amount) + " " + from_currency + " is equal to " + str(converted_amount) + " " + to_currency) 
# DZD --> EUR
elif from_currency == "DZD" and to_currency == "EUR" :
    converted_amount = amount / 270
    print(str(amount) + " " + from_currency + " is equal to " + str(converted_amount) + " " + to_currency)
# GBP --> DZD
elif from_currency == "GBP" and to_currency == "DZD" :
    converted_amount = amount * 310
    print(str(amount) + " " + from_currency + " is equal to " + str(converted_amount) + " " + to_currency)
# DZD --> GBP
elif from_currency == "DZD" and to_currency == "GBP" :
    converted_amount = amount / 310
    print(str(amount) + " " + from_currency + " is equal to " + str(converted_amount) + " " + to_currency)