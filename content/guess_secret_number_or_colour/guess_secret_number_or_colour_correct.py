# Define the secret color and number
secret_color = "blue"
secret_number = 42

while True:
    # Prompt the user to enter 'A' or 'B'
    choice = input("Enter 'A' to guess the secret color or 'B' to guess the secret number: ").strip().upper()
    
    if choice == 'A':
        # Let the user guess the secret color
        color_guess = input("Guess the secret color: ").strip().lower()
        if color_guess == secret_color:
            print("Correct! The secret color is blue.")
            break
        else:
            print("Incorrect! Try again.")
    
    elif choice == 'B':
        # Let the user guess the secret number
        try:
            number_guess = int(input("Guess the secret number: "))
            if number_guess == secret_number:
                print("Correct! The secret number is 42.")
                break
            else:
                print("Incorrect! Try again.")
        except ValueError:
            print("Please enter a valid number.")
    
    else:
        # If the user presses any other key, repeat the loop
        print("Invalid choice. Please enter 'A' or 'B'.")
print("Program finished!")