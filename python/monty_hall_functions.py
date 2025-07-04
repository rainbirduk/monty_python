import pandas as pd
import random as rd
import subprocess as sb


######################
### game variables ###

# set up the three doors (remember zero indexing!)
doors = (1, 2, 3)

# list the possible tactics for the game
tactics = ("switch", "stick")

# create dict to look up results from the boolean outcomes 
results = {True : "Win", False : "Lose"}


######################
### game functions ###

# function to allocate the winning door
def allocate_winning_door():
    return rd.choice(doors) 

# function to allow the contestant to choose a door, or choose one at rd
def choose_initial_door(door_choice = rd.choice(doors)):
    door_choice = int(door_choice)
    while door_choice not in doors:
        print("")
        print("Sorry, but", door_choice, "is not a valid guess.")
        door_choice = int(input("Enter a door number between 1 an 3: "))
    return door_choice

# function to simulate the host giving a hint
def host_gives_a_hint(winning_door, initial_choice):
    host_choices = [door for door in doors if door not in 
                    [winning_door, initial_choice]]
    return rd.choice(host_choices) 

# function to calculate the contestants final choice from their tactic
def choose_tactic(initial_choice, host_hint, tactic):
    if tactic == "switch":
        final_choice = [door for door in doors if door not in 
                        [host_hint, initial_choice]][0]
    else:
        final_choice = initial_choice
    return final_choice

# function to assign the outcome
def assign_outcome(final_choice, winning_door):
    return final_choice == winning_door


############################
### simulation functions ###


# play through automatically the game using rd choices
def play_monty_hall(tactic = rd.choice(tactics)):
    winning_door = allocate_winning_door()
    initial_choice = choose_initial_door()
    host_hint = host_gives_a_hint(winning_door, initial_choice)
    final_choice = choose_tactic(initial_choice, host_hint, tactic)
    outcome = assign_outcome(final_choice, winning_door)
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
def iterate_monty_hall(n_rounds, n_simulations, tactic_allocation = "random"):
    dict_list = []

    # run the simulation, either choosing a tactic at random or alternating between switch and stick
    tactic_pendulum = rd.choice([1,2])
    for sim in range(n_simulations):
        if tactic_allocation == "random":
            tactic = rd.choice(tactics)
        elif tactic_allocation == "equal":
            tactic = tactics[tactic_pendulum % 2]
            tactic_pendulum = tactic_pendulum + 1
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
