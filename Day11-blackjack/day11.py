
import os
import random
from art import logo
 
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
 
def initialize_game():
  run_game()
 
def run_game():
  question_run = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if question_run == 'y':
    start_draw()
  else:
    return False
 
def start_draw():
  os.system('cls' if os.name == 'nt' else 'clear')
  print(logo)
 
  # initial cards and calculating their score - user value
  u_cards = initial_cards()
  c_cards = initial_cards()
  # computer values
  u_score = calculate_score(u_cards)
  c_score = calculate_score(c_cards)
  print_results(u_cards, c_cards, u_score, c_score)
 
  game_continue = True
  while game_continue:
    if u_score < 21 and not c_score == 21:
      next_round = input("Type 'y' to get another card, type 'n' to pass: ")
      if next_round == 'y':
        u_cards.append(deal_card())
        c_cards.append(deal_card())
        u_score = calculate_score(u_cards)
        c_score = calculate_score(c_cards)
        print_results(u_cards, c_cards, u_score, c_score)
      else:
        while c_score < 17:
          new_comp_card = deal_card()
          c_cards.append(new_comp_card)
          c_score += new_comp_card
        are_you_winner(u_cards, c_cards, u_score, c_score)
        game_continue = False
    else:
      are_you_winner(u_cards, c_cards, u_score, c_score)
      game_continue = False
  initialize_game()
 
def are_you_winner(u_cards, c_cards, user_score, comp_score):
  """Take list of cards and there scores to decide if winner/looser. The order matter based on Blackjack rule."""
  if comp_score == 21:
    print("You lose.")
  elif user_score == 21:
    print("You win 😁")
  elif user_score == comp_score:
    print("Draw 🙃")
  elif user_score < comp_score and (user_score < 22 and comp_score < 22):
    print("You lose. 😤")
  elif user_score < comp_score and (user_score < 22 and comp_score > 21):
    print("Opponent went over. You win 😃")
  elif user_score > comp_score and user_score < 22:
    print("You win 😃")
  else:
    print("You went over. You lose 😭")
  # After if statement print final message
  print(f"Your final hand: {u_cards}, final score: {user_score}")
  print(f"Computer's final hand: {c_cards}, final score: {comp_score} \n")
 
def print_results(user_cards, comp_cards, u_score, c_score):
    print(f"Your cards: {user_cards}, current score: {u_score}")
    print(f"Computer's first card: {comp_cards[0]} \n")
  
def initial_cards():
  cards = []
  for i in range(2):
    cards.append(deal_card())
  return cards
 
def deal_card():
  """Randomly chosen number used as a index between 0 and 13, what is length of the cards array"""
  rand_idx = random.randrange(0, 13, 1) 
  return cards[rand_idx]
 
def calculate_score(cards):
  """Take a list of cards and return the calculated score if more than 21 replace ace with 1."""
  if 11 in cards and sum(cards) > 21:
    pos = cards.index(11)
    cards[pos] = 1
  return sum(cards)
 
initialize_game()