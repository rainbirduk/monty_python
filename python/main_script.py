import menu_functions as menu

print()
print("WELCOME TO THE MONTY HALL GAME")
    
def main():
    """
    Launches the Monty Hall game interface and handles user interaction via a menu loop.

    Continuously displays a menu of options and executes the selected task:
        - If the task is a script or function, it is executed via `run_task`.
        - If the user selects 'exit', the loop terminates and a farewell message is printed.

    Menu items and task logic are defined in the `menu_functions` module.
    """
    while True:
        user_selection = menu.menu()
        task_type, _ = menu.items[user_selection][1]
        if task_type != 'exit':
            menu.run_task(menu.items[user_selection][1])     
        else:
            print("\nThanks for playing Monty Hall\n")
            break

if __name__ == "__main__":
    main()
