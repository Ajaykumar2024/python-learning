'''we all have played snakes , water gun  game in childhood. If you haven't , google the rule  of this game '
    and write a python program capable of playing this game with user

    The Snake, Water, Gun game is a simple Python game similar to Rock, Paper, Scissors.

Rules of the Game

There are 3 choices:

1. Snake
2. Water
3. Gun
Winning Rules:-
Player	        Computer	        Result
Snake	        Water	            Snake wins 🐍 (Snake drinks water)
Water	        Gun	                Water wins 💧 (Gun sinks in water)
Gun	            Snake	            Gun wins 🔫 (Gun kills snake)
Same	        Same	            Draw
'''

import random
choices = ['snake', 'water', 'gun']

computer = random.choice(choices)
you = input("Enter your choice (snake, water, gun): ").lower()


print(f"Computer chose: {computer} \nYou chose: {you}")
if you == computer:
    print(f"Both players selected {you}. It's a draw!")
elif you == 'snake' and computer == 'water':
    print("You win!")
elif you == 'snake' and computer == 'gun':
    print("You lose!")
elif you == 'water' and computer == 'gun':
    print("You win!")
elif you == 'water' and computer == 'snake':
    print("You lose!")
elif you == 'gun' and computer == 'snake':
    print("You win!")
elif you == 'gun' and computer == 'water':
    print("You lose!")
else:
    print("Invalid input! Please choose either 'snake', 'water', or 'gun'.")


