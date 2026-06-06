print ("Hello dear, I'll chouse a random number between 1 and 1024, and you have to guess it. Let's start!")
import random
number = random.randint(1, 1024)
guess = 0
while guess != number:
    guess = int(input("Enter your guess: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Congratulations!🎉 You guessed the number.")
