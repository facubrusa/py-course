import random


def choose_options():
  options = ('rock', 'paper', 'scissors')
  user_option = input('Write rock, paper o scissors => ')
  user_option = user_option.lower()

  if not user_option in options:
    print('That option isn\'t valid')
    # continue
    return None, None

  computer_option = random.choice(options)

  print('User option =>', user_option)
  print('Computer option =>', computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('DRAW!')
  elif user_option == 'rock':
    if computer_option == 'scissors':
      print('rock BEATS scissors')
      print('USER WON!')
      user_wins += 1
    else:
      print('paper BEATS a rock')
      print('COMPUTER WON!')
      computer_wins += 1
  elif user_option == 'paper':
    if computer_option == 'rock':
      print('paper BEATS a rock')
      print('USER WON')
      user_wins += 1
    else:
      print('scissors BEATS a paper')
      print('COMPUTER WON!')
      computer_wins += 1
  elif user_option == 'scissors':
    if computer_option == 'paper':
      print('scissors BEATS a paper')
      print('USER WON!')
      user_wins += 1
    else:
      print('rock BEATS a scissors')
      print('COMPUTER WON!')
      computer_wins += 1
  return user_wins, computer_wins

def run_game():
  computer_wins = 0
  user_wins = 0  
  rounds = 1
  while True:
    if (rounds > 1):
      print("\n")
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('Computer wins:', computer_wins)
    print('User wins:', user_wins)
    rounds += 1

    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

    if computer_wins == 2:
      print('\n')
      print('*' * 26)
      print('The winner is the computer')
      print('*' * 26)
      break

    if user_wins == 2:
      print('\n')
      print('*' * 23)
      print('The winner is the user')
      print('*' * 23)
      break

run_game()