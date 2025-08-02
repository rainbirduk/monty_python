import print_and_input_functions as tx
import subprocess as sb

# Define menu items with display text and associated action
# Each entry maps an integer key to:
#   - A string for display in the menu
#   - A tuple specifying the action type ('script', 'function', or 'exit') and the corresponding target
items = {
    1: ['| 1. Play the Monty Hall Game', ('script', 'play_monty_hall.py')],
    2: ['| 2. Run a Monty Hall simulation', ('script', 'run_user_simulation.py')],
    3: ['| 3. Check the rules and standard assumptions', ('function', tx.print_rules)],
    4: ['| 4. Learn more about Monty Hall', ('function', tx.open_wiki)],
    5: ['| 5. Function test', ('script', 'monty_hall_functions_test.py')],
    6: ['| 6. Quit the game', ('exit', None)]
}

# Create a list of valid menu option keys for input validation and iteration
item_index = list(items.keys())

def menu():
    """
    Displays a menu of options and prompts the user to make a selection.

    The function prints a numbered list of menu items defined in the global `items` list,
    using indices from the global `item_index` list. It repeatedly prompts the user until
    a valid selection is made (i.e., an integer corresponding to one of the listed indices).

    Returns:
        int: The index of the selected menu item.
    """
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
            user_selection = None  # Reset user_selection to stay in the loop
    return user_selection

def run_task(task):
    """
    Executes a given task based on its type and waits for user confirmation to return.

    The task should be a tuple containing:
        - task_type (str): Either 'script' or 'function'.
        - action: A string representing the script filename (if task_type is 'script'),
                  or a callable function (if task_type is 'function').

    Behavior:
        - If task_type is 'script', runs the specified Python script using subprocess.
        - If task_type is 'function', calls the provided function directly.
        - After execution, prompts the user to press Enter before returning to the main menu.

    Args:
        task (tuple): A (task_type, action) pair specifying what to run.
    """
    task_type, action = task
    if task_type == 'script':
        sb.run(['python', action])
    elif task_type == 'function':
        action()
    print("")
    input("Press Enter to return to the main menu...")
    print("___________________________________________")