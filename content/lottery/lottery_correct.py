import random
import time

print("Welcome to the lottery")

user_numbers = []
print("Enter five unique numbers between 1 and 20:")

while len(user_numbers) < 5:
    num = int(input(f"Enter number {len(user_numbers) + 1}: "))
    if num < 1 or num > 20:
        print("Number must be between 1 and 20.")
    elif num in user_numbers:
        print("Number must be unique.")
    else:
        user_numbers.append(num)


# Randomise five numbers between 1 and 20
lottery_numbers = random.sample(range(1, 21), 5)

# Simulate the lottery draw with pauses
print("Drawing lottery numbers...")
for number in lottery_numbers:
    time.sleep(1) 
    print(number)

# Check how many numbers match
matches = len(set(user_numbers) & set(lottery_numbers))

# Output the result
if matches == 5:
    print("You've won the lottery!!")
else:
    print(f"You have {matches} matching numbers.")