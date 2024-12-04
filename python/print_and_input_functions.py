import monty_hall_functions as mh
import subprocess as sb
from rich.console import Console
cs = Console()

# function to underline text for titles
def print_underlined(text):
    cs.print(text, style = "underline")

# print the introduction text
def print_intro():
    print("")
    print("You are on a game show and the host presents you with three boxes.")
    print("Inside one box are the keys to a new Suzuki sports bike; the other two boxes are empty.")

# print the rules
def print_rules():
    print("")
    print("The game runs like this:")
    print("1. The contestant first chooses a box but does not open it")
    print("2. The host gives a hint that is niether the winning box nor the initial_choice")
    print("3. The contestant decides whether or not to switch their choice to the remaining box")
    print("4. Their final choice box is opened to reveal the outcome of the game")

# print the assumptions
def print_assumptions():
    print("")
    print("Standard assumptions:")
    print("- The prize is equally likely to be behind any door.")
    print("- The host will always open a box that the contestant did not choose.")
    print("- The host will always reveal an empty box and never the winning box.")
    print("- If the contestant's first choice is correct, the host will always reveal from the remaining boxes at random.")

# make a dict to express numbers as words
box_text_dict = {1: "ONE", 2: "TWO", 3: "THREE"}

# input functions for the contestants initial choice of box
def input_initial_choice():
    print("")
    print("The host invites you to choose a box that you think might be the winner")
    initial_choice = input("Choose a box by entering a number between 1 and 3: ")
    initial_choice = mh.choose_initial_box(initial_choice)
    print("")
    print("You have chosen box number", box_text_dict[initial_choice])
    return initial_choice

# print the host hints
def print_host_hint(host_hint):
    print("")
    print("Without opening your chosen box, the host proceeds to open box number", 
        box_text_dict[host_hint], "to reveal that it is empty.")
    
# function to allow contestant to interactively choose and confirm their tactic
def input_choose_and_confirm_tactic(initial_choice, host_hint):

    # host invites contestant to switch their choice
    print("The host then invites you to switch your choice to the remaining box")
    
    # contestant chooses a strategy
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
    return final_choice

# print the game outcome
def print_game_outcome(final_choice, winning_box):
    
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