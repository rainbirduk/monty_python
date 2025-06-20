import subprocess as sb

# set up a selection of menu items and associated script names
items = {1 : ['| 1. Play the Monty Hall Game',                     'play_monty_hall.py'],
         2 : ['| 2. Run a Monty Hall simulation',                  'simulate_monty_hall.py'],
         3 : ['| 3. Check the rules and standard assumptions',     'print_rules_and_assumptions.py'],
         4 : ['| 4. Learn more about Monty Hall',                  'monty_hall_analysis_placeholder.py'],
         5 : ['| 5. Function test',                                'monty_hall_functions_test.py'],
         6 : ['| 6. Quit the game',                                'NA']}

# make a menu index
item_index = list(items.keys())

# function to prompt for and return a menu selection from the user
def menu():
    
    print("")
    print("Main menu")
    print("What would you like to do?")

    user_selection = None
    while user_selection == None:
        for i in item_index:
            print(items[i][0])
        try:
            user_selection = int(input("Please make your selection: "))
            if user_selection not in item_index:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a number from the menu: ")
            user_selection = None  # Reset user_selection to stay in the loop
    return user_selection

# wrapper function to run the chosen script and then pause to prompt before returning to manin menu
def run_script(script_name):
    sb.run(['python', script_name])
    input("\nPress Enter to return to the main menu...")
    print("___________________________________________")
    print("")
    print("What would you like to do now?")