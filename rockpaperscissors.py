import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

print("Welcome to the best game every created! Rock, Paper, Scissors!\n")

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

opponent_choice = random.choice([0, 1, 2])

if player_choice == 0:
    if opponent_choice == 0:
        print(f"{rock} vs {rock}\n It's a tie!")
    elif opponent_choice == 1:
        print(f"{rock} vs {paper}\n You lose!")
    else:
        print(f"{rock} vs {scissors}\n You win!")
elif player_choice == 1:
    if opponent_choice == 0:
        print(f"{paper} vs {rock}\n You win!")
    elif opponent_choice == 1:
        print(f"{paper} vs {paper}\n It's a tie!")
    else:
        print(f"{paper} vs {scissors}\n You lose!")
elif player_choice == 2:
    if opponent_choice == 0:
        print(f"{scissors} vs {rock}\n You lose!")
    elif opponent_choice == 1:
        print(f"{scissors} vs {paper}\n You win!")
    else:
        print(f"{scissors} vs {scissors}\n It's a tie!")

 
 
