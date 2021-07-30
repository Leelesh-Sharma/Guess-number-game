import random

print("Secret number")

print("Enter two numbers in which your secret number lies:")
a = int(input("First number: "))
b = int(input("Second number: "))
print(f"Your secret number lies in between {a} and {b}. Try to Guess it.")

secretNumber = random.randint(a, b)
guessing = 0
count = 0

while guessing != secretNumber:
     guessing = int(input(">>> "))
     count = count + 1
     print("Wrong!!")

print(f"You win. on your {count} try")
