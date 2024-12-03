import subprocess as sb

print("")
print("WELCOME TO THE MONTY HALL GAME")
    
# set up a selection of menu items and associated script names
menu_items = {1 : ['| 1. Play the Monty Hall Game',                     'play_monty_hall.py'],
              2 : ['| 2. Run a Monty Hall simulation',                  'simulate_monty_hall.py'],
              3 : ['| 3. Read a statistical analysis of Monty Hall',    'monty_hall_analysis_placeholder.py'],
              4 : ['| 4. Check the rules and standard assumptions',     'print_rules_and_assumptions.py'],
              5 : ['| 5. Function test',                                'monty_hall_functions_test.py'],
              6 : ['| 6. Quit the game',                                'NA']}

# make a menu index
menu_index = list(range(1, len(menu_items) + 1))

# function to prompt for and return a menu selection from the user
def main_menu():
    
    print("")
    print("Main menu")
    print("What would you like to do?")

    user_selection = None
    while user_selection == None:
        for index in menu_index:
            print(menu_items[index][0])
        print("")
        try:
            user_selection = int(input("Please make your selection: "))
            if user_selection not in menu_index:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a number from the menu: ")
            user_selection = None  # Reset user_selection to stay in the loop

    return user_selection

# wrapper function to run the chosen script and then prompt return to manin menu
def run_script(script_name):
    sb.run(['python', script_name])
    input("\nPress Enter to return to the main menu...")
    print("___________________________________________")
    print("")
    print("What would you like to do now?")

# main script
def main():
    while True:
        user_selection = main_menu()
         
        if user_selection < len(menu_items):
            run_script(menu_items[user_selection][1])
        
        else:
            print("")
            print("Thanks for playing the Monty Hall game")
            print("This little project is dedicated to Marilyn vos Savant, a magazine columnist", 
                  "with an IQ of 228 who faced down 1,000 PhD's to solve the Monty Hall problem.")
            print("")
            break

if __name__ == "__main__":
    main()

