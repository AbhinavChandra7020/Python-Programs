import random

list1 = ["rock", "paper", "scissor"]  # Making a list of all possible choices for the computer
print("if you want to end the game type done")
while True:
    inp = input('Enter rock paper or scissor \n')
    if inp == 'done':
        break
    ch = random.choice(list1)  # Letting the computer make a choice against the user
    ch = ch.lower()
    ch.strip()
    print(ch)
    if ch == inp:  # Comparing choices between user and the computer
        print("Go again")
        continue
    if (inp == 'rock' and ch == 'scissor') or (inp == 'paper' and ch == 'rock') or (
            inp == 'scissor' and ch == 'paper'):  # Win Condition
        print("You won")
        break
    if (inp == 'rock' and ch == 'paper') or (inp == 'paper' and ch == 'scissor') or (
            inp == 'scissor' and ch == 'paper'):  # Loss Condition
        print("You lost")
        break
print("Game Over")
