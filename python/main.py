import menu_functions as menu

print("")
print("WELCOME TO THE MONTY HALL GAME")
    
def main():
    while True:
        user_selection = menu.menu()
         
        if user_selection < len(menu.items):
            menu.run_script(menu.items[user_selection][1])
        
        else:
            break

if __name__ == "__main__":
    main()

