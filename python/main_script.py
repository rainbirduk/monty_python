import menu_functions as menu

print("")
print("WELCOME TO THE MONTY HALL GAME")
    
def main():
    while True:
        user_selection = menu.menu()
        if user_selection != 6:
            menu.run_script(menu.items[user_selection][1])      
        else:
            print("")
            print("Thanks for playing Monty Hall")
            print("")
            break

if __name__ == "__main__":
    main()
