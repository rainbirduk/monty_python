# import modules
import monty_hall_functions as mh
import random as rd

from rich.console import Console
cs = Console()

# winning door
winning_door = mh.allocate_winning_door()

# # contestant chooses a door
initial_choice = mh.choose_initial_door()

# host gives a hint that is not winning_door or initial_choice
host_hint = mh.host_gives_a_hint(winning_door, initial_choice)

# the contestant decides a tactic
tactic = rd.choice(mh.tactics)

# calculate the contestants final choice from their tactic
final_choice = mh.choose_tactic(initial_choice, host_hint, tactic)

# assign the oucome
outcome = mh.assign_outcome(final_choice, winning_door)

# simulation outcomes
print("")
cs.print("Function outputs", style = "underline")
print("          doors:", mh.doors)
print("    winning_door:", winning_door)
print(" initial_choice:", initial_choice)
print("      host_hint:", host_hint)
print("         tactic:", tactic)
print("   final_choice:", final_choice)
print("         result:", mh.results[outcome])
print("")

#simulate a single game
single_simulation_results = mh.simulate_monty_hall(5)
cs.print("Output for a single simulation", style = "underline")
print(single_simulation_results)

# summarise the results of a single game
single_simulation_summary = mh.summarise_game_simulation(single_simulation_results)
print("")
cs.print("Summary for the same simulation", style = "underline")
print(single_simulation_summary)

# iterate simulation and produce a dataset
multi_simulation_df = mh.iterate_monty_hall(50, 5)
print("")
cs.print("Summary for multiple simulations", style = "underline")
print(multi_simulation_df)
print("")




