import print_and_input_functions as tx
import subprocess as sb

# Define menu items with type and action
items = {
    1: ['| 1. Play the Monty Hall Game', ('script', 'play_monty_hall.py')],
    2: ['| 2. Run a Monty Hall simulation', ('script', 'run_user_simulation.py')],
    3: ['| 3. Check the rules and standard assumptions', ('function', tx.print_rules)],
    4: ['| 4. Learn more about Monty Hall', ('function', tx.open_wiki)],
    5: ['| 5. Function test', ('script', 'monty_hall_functions_test.py')],
    6: ['| 6. Quit the game', ('exit', None)]
}

# make a menu index
item_index = list(items.keys())

# function to prompt for and return a menu selection from the user
def menu():
    print("\nMain menu")
    print("What would you like to do?")

    user_selection = None
    while user_selection is None:
        for i in item_index:
            print(items[i][0])
        try:
            user_selection = int(input("\nPlease make your selection: "))
            if user_selection not in item_index:
                raise ValueError
        except ValueError:
            print("\nInvalid input. Please enter a number from the menu: ")
            user_selection = None  # reset user_selection to stay in the loop
    return user_selection

# wrapper function to run the chosen script and then pause to prompt before returning to manin menu
def run_task(task):
    task_type, action = task
    if task_type == 'script':
        sb.run(['python', action])
    elif task_type == 'function':
        action()
    print("")
    input("Press Enter to return to the main menu...")
    print("___________________________________________")