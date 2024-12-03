# import modules
import monty_hall_functions as mh
import random as rd

# introduction
print("")
print("You are on a game show and the host presents you with three boxes.")
print("Inside one box are the keys to a new sports bike; the other two boxes are empty.")

# winning box
winning_box = rd.choice(mh.boxes) 

# make a dict to express numbers as words
box_text_dict = {1: "ONE", 2: "TWO", 3: "THREE"}

# # contestant chooses a box
print("")
print("The host invites you to choose a box that you think might be the winner")
initial_choice = input("Choose a box by entering a number between 1 and 3: ")
initial_choice = mh.choose_initial_box(initial_choice)
print("")
print("You have chosen box number", box_text_dict[initial_choice])

# host gives a hint that is not winning_box or initial_choice
host_hint = mh.host_gives_a_hint(winning_box, initial_choice)
print("")
print("Without opening your chosen box, the host proceeds to open box number", 
      box_text_dict[host_hint], "to reveal that it is empty.")

# host invites contestent to switch or stick
print("She then invites you to switch your choice to the remaining box")

# contestant chooses tactic
check = "n"
while check[0].lower() == "n":
    print("")
    tactic = input("Would you like to switch or stick? ").lower()
    final_choice = mh.choose_tactic(initial_choice, host_hint, tactic)

    # double check the contestants tactic
    print("")
    if final_choice == initial_choice:
        print("Are you sure you want to stick with box number", box_text_dict[initial_choice])
    else:
        print("Are you sure you want to switch from box number", box_text_dict[initial_choice],
              "to box number", box_text_dict[final_choice])
    check = input("Please enter either 'yes' or 'no': ")
    while check[0].lower() not in ["y", "n"]:
        print("")
        print(check, "is not a valid option.")
        check = input("Please enter either 'yes' or 'no': ")

# assign final tactic
if  tactic == "stick":
    final_choice = initial_choice

# assign the oucome
outcome = mh.assign_outcome(final_choice, winning_box)

# assign the result
print("")
if outcome:
    print(f"You win! The winning box was indeed box number {box_text_dict[winning_box]}!")
    print("Thanks for playing. Enjoy your sports bike.")
else:
    print(f"You have lost :( The winning box was box number {box_text_dict[winning_box]}.")
    print("Thanks for playing. Better luck next time.")
print("")





