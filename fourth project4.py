# This is a password generator that creates a random password based on user input for length and how many of passwords to generate, or check the strength of a password.
#  It uses the secrets module for secure random generation and the string module for character sets.
import secrets
import string
import random
user_input = input("Welcome to the password generator! " 
"Do you want to '(1):generate a password' or '(2):check the strength of a password'? (Type '1' or '2') ")
#=================
# generating part
#=================
if user_input == "1":
    length = int(input("How long do you want your password to be? "))
    num_passwords = int(input("how many passwords do you want to generate? "))
    for _ in range(num_passwords):
        password = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        print("Generated password:", password)
#===============        
# checking part          
#===============
else: user_input == "2"
password_to_check = input("Enter the password you want to check: ")

has_lower = False
has_upper = False
has_digit = False
has_special = False

for char in password_to_check:
    if char in string.ascii_lowercase:
        has_lower = True
    elif char in string.ascii_uppercase:
        has_upper = True
    elif char in string.digits:
        has_digit = True
    elif char in string.punctuation:
        has_special = True

score = 0

if has_lower:
    score += 1
else:
    print("Missing lowercase letters.")

if has_upper:
    score += 1
else:
    print("Missing uppercase letters.")

if has_digit:
    score += 1
else:
    print("Missing digits.")

if has_special:
    score += 1
else:
    print("Missing special characters.")

if len(password_to_check) >= 16:
    score += 1
else:
    print("Password should be at least 12 characters long.")

print(f"\nScore: {score}/5")

if score <= 2:
    print("Strength: Weak")
elif score <= 4:
    print("Strength: Medium")
else:
    print("Strength: Strong")