import pandas as pd
import random as rd
import subprocess as sb


######################
### game variables ###

# set up the three boxes (remember zero indexing!)
boxes = (1, 2, 3)

# list the possible tactics for the game
tactics = ("switch", "stick")

# create dict to look up results from the boolean outcomes 
results = {True : "Win", False : "Lose"}


######################
### game functions ###

# function to allocate the winning box
def allocate_winning_box():
    return rd.choice(boxes) 

# function to allow the contestant to choose a box, or choose one at rd
def choose_initial_box(box_choice = rd.choice(boxes)):
    box_choice = int(box_choice)
    while box_choice not in boxes:
        print("")
        print("Sorry, but", box_choice, "is not a valid guess.")
        box_choice = int(input("Enter a box number between 1 an 3: "))
    return box_choice

# function to simulate the host giving a hint
def host_gives_a_hint(winning_box, initial_choice):
    host_choices = [box for box in boxes if box not in 
                    [winning_box, initial_choice]]
    return rd.choice(host_choices) 

# function to calculate the contestants final choice from their tactic
def choose_tactic(initial_choice, host_hint, tactic):
    while tactic not in tactics:
        print("")
        tactic = input("Invalid tactic; please enter 'switch' or 'stick': ")
    if tactic == "switch":
        final_choice = [box for box in boxes if box not in 
                        [host_hint, initial_choice]][0]
    else:
        final_choice = initial_choice
    return final_choice

# function to assign the outcome
def assign_outcome(final_choice, winning_box):
    return final_choice == winning_box


############################
### simulation functions ###

# play through automatically the game using rd choices
def play_monty_hall(tactic = rd.choice(tactics)):
    winning_box = allocate_winning_box()
    initial_choice = choose_initial_box()
    host_hint = host_gives_a_hint(winning_box, initial_choice)
    final_choice = choose_tactic(initial_choice, host_hint, tactic)
    outcome = assign_outcome(final_choice, winning_box)
    return {"tactic" : tactic, "result" : results[outcome]}

# function to simulate n rounds of a monty hall game with one tactic
def simulate_monty_hall(n_rounds = 5, tactic = rd.choice(tactics)):
    dict_list = []
    for round in range(n_rounds):
        result = play_monty_hall(tactic) 
        dict_list.append(result)
    df = pd.DataFrame(dict_list)
    return df
 
# function to calculate the win rate
def summarise_game_simulation(simulation_results):
    tactic = simulation_results["tactic"][0]
    total_wins = simulation_results[simulation_results['result'] == 'Win'].shape[0]
    total_rounds = simulation_results.shape[0]
    win_rate = total_wins / total_rounds
    summary_dict = {"tactic" : tactic, "success_rate" : win_rate}
    return summary_dict

# iterate n simulations with n rounds
def iterate_monty_hall(n_rounds, n_simulations):
    dict_list = []
    for sim in range(n_simulations):
        tactic = rd.choice(tactics)
        simulation_results = simulate_monty_hall(n_rounds, tactic) 
        simulation_summary = summarise_game_simulation(simulation_results)
        dict_list.append(simulation_summary)
    df = pd.DataFrame(dict_list)
    return df


###############
### testing ###

# test the functions if run directly
if __name__ == "__main__":
    sb.run(['python', 'monty_hall_functions_test.py'])
