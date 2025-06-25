import monty_hall_functions as mh
import subprocess as sb
import webbrowser as wb
from rich.console import Console
cs = Console()

# function to underline text for titles
def print_underlined(text):
    cs.print(text, style = "underline")

# print the introduction
def print_intro():
    print("")
    try:
        with open('../text/game_intro.txt', 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("The intro text file could not be found.")

# print the rules
def print_rules():
    try:
        with open('../text/game_rules.txt', 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("The rules text file could not be found.")

# open a browser and go to the monty hall wikipedia article
def open_wiki():
    wb.open('https://en.wikipedia.org/wiki/Monty_Hall_problem')

# make a dict to express numbers as words
box_text_dict = {1: "ONE", 2: "TWO", 3: "THREE"}

# input functions for the contestants initial choice of box
def input_initial_choice():
    print("The host invites you to choose a box that you think might be the winner")
    print("")
    initial_choice = input("Choose a box by entering a number between 1 and 3, or type 'rules' for a reminder of the rules and assumptions: ")
    while initial_choice == "rules":
        print("")
        print_rules()
        print("")
        initial_choice = input("Now choose a box by entering a number between 1 and 3: ")
    initial_choice = mh.choose_initial_box(initial_choice)
    print("")
    print("You have chosen box number", box_text_dict[initial_choice])
    return initial_choice

# print the host hints
def print_host_hint(host_hint):
    print("")
    print("Without opening your chosen box, the host proceeds to open box number", 
        box_text_dict[host_hint], "to reveal that it contains a toilet seat.")
    
# function to allow contestant to interactively choose and confirm their tactic
def input_choose_and_confirm_tactic(initial_choice, host_hint):

    # host invites contestant to switch their choice
    print("The host then invites you to switch your choice to the remaining box")
    
    # contestant chooses a strategy
    tactic_confirmed = "n"
    while tactic_confirmed[0].lower() != "y":
        print("")
        tactic = input("Would you like to switch or stick? ").lower()
        while tactic not in mh.tactics:
            print("")
            tactic = input("Invalid tactic; please enter 'switch' or 'stick': ")
        final_choice = mh.choose_tactic(initial_choice, host_hint, tactic)

        # double check the contestants tactic
        print("")
        if final_choice == initial_choice:
            print("Are you sure you want to stick with box number", box_text_dict[initial_choice])
        else:
            print("Are you sure you want to switch from box number", box_text_dict[initial_choice],
                "to box number", box_text_dict[final_choice])
        tactic_confirmed = input("Please enter either 'yes' or 'no': ")
        while tactic_confirmed[0].lower() not in ["y", "n"]:
            print("")
            print(tactic_confirmed, "is not a valid option.")
            tactic_confirmed = input("Please enter either 'yes' or 'no': ")

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

# choose the number of simulations to perform
def choose_n_simulations():
    print("")
    n_simulations = int(input(f"How many simulations of Monty Hall would you like to perform? "))
    return n_simulations

# choose the number of rounds to play per simulation
def choose_n_games():
    print("")
    n_games = int(input("And how many games would you like to play per simulation? "))
    return n_games

# choose whether tactics should be chosen equally or at random. 
def allocate_tactic():
    print("")
    tactic_allocation_options = {"e" : "equal", "r" : "random"}
    tactic_allocation = input("Lastly, would you like to allocate tactics at random or equally across simulations? ")
    while tactic_allocation.lower()[0] not in list(tactic_allocation_options.keys()):
        print("")
        tactic_allocation = input(f"{tactic_allocation} is not a valid choice. Please enter 'equal' or 'random': ")
    tactic_allocation = tactic_allocation_options[tactic_allocation.lower()[0]]
    return tactic_allocation

# function to get ordinal suffixes
def ordinal(n):
    if 10 <= n % 100 <= 13:
        return f"{n}th"
    else:
        return f"{n}{['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]}"