import os
from art import logo, vs
from game_data import data
import random

os.system('cls||clear')  # Clear the screen


def format_data(account):
    """Take the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts, and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display the art
print(logo)
score = 0
game_should_continue = True
# making account at position B become the next account at position A
account_b = random.choice(data)

# Make the game repeatable
while game_should_continue:
    # generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    # format account data into printable format: name, description and country
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # check if user is correct

    # get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # clear the screen between rounds
    os.system('cls||clear')

    # use if statement to check if user is correct
    # give user feedback on their guess
    if is_correct:
        print("You're right!")
    # score keeping
        score += 1
    else:
        game_should_continue = False
        print("Sorry, that's wrong.")
        print(f"Final score {score}.")
