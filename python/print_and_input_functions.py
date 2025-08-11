import monty_hall_functions as mh
from rich.console import Console
import webbrowser as wb

cs = Console()

# Maps door numbers to display labels
door_text_dict = {1: "ONE", 2: "TWO", 3: "THREE"}  

def print_underlined(text):
    """Prints text with underline styling."""
    cs.print(text, style = "underline")

def print_intro():
    """
    Prints the introductory text for the Monty Hall game.

    Attempts to read and display content from '../text/game_intro.txt'.
    If the file is not found, prints a fallback error message.

    Raises:
        FileNotFoundError: Handled internally with a user-friendly message.
    """
    print("")
    try:
        with open('../text/game_intro.txt', 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("The intro text file could not be found.")

def print_rules():
    """
    Displays the rules of the Monty Hall game.

    Reads and prints the contents of '../text/game_rules.txt'.
    If the file is missing, prints an error message instead.

    Raises:
        FileNotFoundError: Handled internally with a user-friendly message.
    """
    print()
    try:
        with open('../text/game_rules.txt', 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("The rules text file could not be found.")

def print_intro_and_rules():
    """
    Prints the introductory text and rules for the Monty Hall game.

    Displays a styled heading, followed by the contents of the intro and rules text files.
    Uses `print_underlined()` for formatting, and calls `print_intro()` and `print_rules()`.
    """
    print()
    print_underlined("The Monty Hall game rules and assumptions")
    print_intro()
    print_rules()

def open_wiki():
    """Opens the Monty Hall problem Wikipedia page in the default web browser."""
    wb.open('https://en.wikipedia.org/wiki/Monty_Hall_problem')

def input_initial_choice():
    """
    Prompts the player to choose an initial door in the Monty Hall game.

    Offers the option to view the game rules before making a selection.
    Accepts input as a string and delegates validation and conversion to `mh.choose_initial_door()`.

    Returns:
        int: The validated door number chosen by the player (1, 2, or 3).
    """
    print("The host invites you to choose a door that you think might be the winner")
    print("")
    initial_choice = input("Choose a door by entering a number between 1 and 3, or type 'rules' for a reminder of the rules and assumptions: ")
    while initial_choice == "rules":
        print_rules()
        print("")
        initial_choice = input("Now choose a door by entering a number between 1 and 3: ")
    initial_choice = mh.choose_initial_door(initial_choice)
    print("")
    print("You have chosen door number", door_text_dict[initial_choice])
    return initial_choice

def print_host_hint(host_hint: int):
    """
    Prints the host's action of revealing a goat behind one of the non-chosen doors.

    Args:
        host_hint (int): The door number (1, 2, or 3) that the host opens to reveal a goat.
    """
    print("")
    print("Without opening your chosen door, the host proceeds to open door number", 
        door_text_dict[host_hint], "to reveal that it contains a goat.")
    
def input_choose_and_confirm_tactic(initial_choice: int, host_hint: int):
    """
    Allows the contestant to interactively choose and confirm their tactic in the Monty Hall game.

    The host invites the contestant to switch doors. The player selects either 'switch' or 'stick',
    and is then asked to confirm their decision. Input is validated and the final choice is determined
    using `mh.choose_tactic()`.

    Args:
        initial_choice (int): The door number initially chosen by the contestant.
        host_hint (int): The door number revealed by the host to contain a goat.

    Returns:
        int: The final door number selected by the contestant after confirming their tactic.
    """

    # host invites contestant to switch their choice
    print("The host then invites you to switch your choice to the remaining door")
    
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
            print("Are you sure you want to stick with door number", door_text_dict[initial_choice])
        else:
            print("Are you sure you want to switch from door number", door_text_dict[initial_choice],
                "to door number", door_text_dict[final_choice])
        tactic_confirmed = input("Please enter either 'yes' or 'no': ")
        while tactic_confirmed[0].lower() not in ["y", "n"]:
            print("")
            print(tactic_confirmed, "is not a valid option.")
            tactic_confirmed = input("Please enter either 'yes' or 'no': ")

    # assign final tactic
    if  tactic == "stick":
        final_choice = initial_choice
    return final_choice

def print_game_outcome(final_choice: int, winning_door: int):
    """
    Displays the outcome of the Monty Hall game based on the player's final choice.

    Determines whether the player has won or lost using `mh.assign_outcome()`,
    then prints a corresponding message. 

    Args:
        final_choice (int): The door number selected by the player after confirming their tactic.
        winning_door (int): The door number that contains the prize.

    Side Effects:
        - Prints outcome messages to the console.
    """   
    outcome = mh.assign_outcome(final_choice, winning_door)
    if outcome:
        print(f"\nYou win! The winning door was indeed door number {door_text_dict[winning_door]}!")
    else:
        print(f"\nYou have lost :( The winning door was door number {door_text_dict[winning_door]}.")
    print("Thanks for playing.")
    
def choose_n_simulations() -> int:
    """
    Prompts the user to enter the number of Monty Hall simulations to run.

    Returns:
        int: The number of simulations specified by the user.
    """
    print("")
    n_simulations = int(input(f"How many simulations of Monty Hall would you like to perform? "))
    return n_simulations

def choose_n_games() -> int:
    """
    Prompts the user to enter the number of games to play per simulation.

    Returns:
        int: The number of games specified by the user.
    """
    print("")
    n_games = int(input("And how many games would you like to play per simulation? "))
    return n_games

def allocate_tactic() -> str:
    """
    Prompts the user to choose how tactics should be allocated across simulations.

    The user may enter 'equal' or 'random' (case-insensitive). If the input is invalid,
    the function will repeatedly prompt until a valid choice is entered.

    Returns:
        str: The selected tactic allocation method, either 'equal' or 'random'.
    """
    print("")
    tactic_allocation_options = {"e" : "equal", "r" : "random"}
    tactic_allocation = input("Lastly, would you like to allocate tactics at random or equally across simulations? ")
    while tactic_allocation.lower()[0] not in list(tactic_allocation_options.keys()):
        print("")
        tactic_allocation = input(f"{tactic_allocation} is not a valid choice. Please enter 'equal' or 'random': ")
    tactic_allocation = tactic_allocation_options[tactic_allocation.lower()[0]]
    return tactic_allocation

def ordinal(n: int) -> str:
    """
    Returns the ordinal representation of an integer.

    For example, 1 becomes '1st', 2 becomes '2nd', 3 becomes '3rd', and so on.

    Args:
        n (int): The integer to convert.

    Returns:
        str: The ordinal string corresponding to the input integer.
    """
    if 10 <= n % 100 <= 13:
        return f"{n}th"
    else:
        return f"{n}{['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]}"