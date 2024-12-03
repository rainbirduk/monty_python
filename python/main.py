import menu_functions as menu

print("")
print("WELCOME TO THE MONTY HALL GAME")
    
def main():
    while True:
        user_selection = menu.menu()
         
        if user_selection < len(menu.items):
            menu.run_script(menu.items[user_selection][1])
        
        else:
            print("")
            print("Thanks for playing the Monty Hall game")
            print("This little project is dedicated to Marilyn vos Savant, a magazine columnist", 
                  "with an IQ of 228 who faced down 1,000 PhD's to solve the Monty Hall problem.")
            print("")
            break

if __name__ == "__main__":
    main()

