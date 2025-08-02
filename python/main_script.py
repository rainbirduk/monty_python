import menu_functions as menu

print("")
print("WELCOME TO THE MONTY HALL GAME")
    
def main():
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
