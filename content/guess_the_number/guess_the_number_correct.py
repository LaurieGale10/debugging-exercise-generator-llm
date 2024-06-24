import random

def get_unique_numbers(players):
    numbers = {}
    for player in players:
        while True:
            num = int(input(f"Player {player}, choose a number between 1 and 100: "))
            if num < 1 or num > 100 or num in numbers.values():
                print("Invalid input or number already taken. Try again.")
            numbers[player] = num
            break
    return numbers

players = ['A', 'B', 'C', 'D', 'E']

while len(players) > 1:
    print("\nNew Round")
    numbers = get_unique_numbers(players)
    random_number = random.randint(1, 100)
    print(f"Random Number: {random_number}")

    differences = {player: abs(num - random_number) for player, num in numbers.items()}
    furthest_player = max(differences, key=differences.get)
    
    print(f"Player {furthest_player} is out (Difference: {differences[furthest_player]})")
    players.remove(furthest_player)

print(f"\nPlayer {players[0]} is the winner!")