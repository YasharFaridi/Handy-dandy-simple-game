""" 
    Crated by YasharFaridi      (Monday, February 1, 2021, 3:18PM)
    this script is simple GOl ya pooch game 
            enjoy it!
"""

# Real GOl ya Pooch game

from random import shuffle

print("\nWellcom to the Gol ya pooch game.")
print("RULES: If you want to win you should awnser correctly mor than three times.\n")

number_of_choice = int(input("How many want have choice: "))
number_of_rounds = int(input("How many round do you want play: "))
print()
print("-" * 50, "\n")

gol = ["*"]
pooch = ["-"]
awnsers = ["Yes", "YES", "yes", "Y", "y"]

rand_gol = 0
number_of_wins = 0
number_of_wins_again = 0

for i in range(0, number_of_choice - 1):
    gol.append("-")
    pooch.append("-")

shuffle(gol)

while number_of_rounds > 0:
    for num in range(1, number_of_choice + 1):
        print(f"{num}", end="     ")
    print()

    for p in range(0, number_of_choice):
        print(f"{pooch[p]:6}", end="")
    print()

    print(f"You have {number_of_rounds} time to play (Carfull!)")
    user_awnser = int(input(f"\n{number_of_rounds}. Do your guess where is the star: "))

    i = 1
    for awnser in gol:
        if awnser == "*":
            rand_gol = i
        i += 1

    if user_awnser > number_of_choice:
        print("You can't select it! try again.")
        continue

    if user_awnser == rand_gol:

        print("\n\tRight awnser.")
        for num in range(1, number_of_choice + 1):
            print(f"{num}", end="     ")
        print()

        for g in range(0, number_of_choice):
            print(f"{gol[g]:6}", end="")
        print()

        number_of_wins += 1
        
    else:
        print(f"\n\tWrong awnser.")
        print(f"The awnser was:")

        for num in range(1, number_of_choice + 1):
            print(f"{num}", end="     ")
        print()

        for g in range(0, number_of_choice):
            print(f"{gol[g]:6}", end="")
        print()

    number_of_rounds -= 1

    print(f"\nYour right awnser >>> {number_of_wins}\n")

    if number_of_wins == 3 and number_of_rounds > 0:
        print(f"You guess {number_of_wins} correctly.")
        print(f"\n(you can play {number_of_rounds} time(s) more) .")
        play_again = input(f"You win \t Do you want play more time Yes or no (N \ Y):")
        print()

        if play_again in awnsers:
            number_of_wins_again = number_of_wins
            number_of_wins = 0
        else:
            break

    shuffle(gol)

wins = number_of_wins_again + number_of_wins

if wins >= 3:
    print(f"You guess {wins} times correctly.")
    print("And you win.\n")
    print("-" * 50)
else:
    print("You loose!")
    print(f"You guess {wins} time/times correctly.\n")
    print("-" * 50)

print("\nThe End.\n")
