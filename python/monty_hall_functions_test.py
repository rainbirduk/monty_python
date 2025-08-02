import monty_hall_functions as mh
import random as rd

from rich.console import Console
cs = Console()

# Run core Monty Hall functions individually for basic testing
winning_door = mh.allocate_winning_door()
initial_choice = mh.choose_initial_door()
host_hint = mh.host_gives_a_hint(winning_door, initial_choice)
tactic = rd.choice(mh.tactics)
final_choice = mh.choose_tactic(initial_choice, host_hint, tactic)
outcome = mh.assign_outcome(final_choice, winning_door)

# Display the outputs of individual function calls
print()
cs.print("Function outputs", style = "underline")
print("          doors:", mh.doors)
print("    winning_door:", winning_door)
print(" initial_choice:", initial_choice)
print("      host_hint:", host_hint)
print("         tactic:", tactic)
print("   final_choice:", final_choice)
print("         result:", mh.results[outcome])
print()

# Run and display results from a single simulation of multiple rounds
single_simulation_results = mh.simulate_monty_hall(5)
cs.print("Output for a single simulation", style = "underline")
print(single_simulation_results)

# Summarize win rate from the single simulation
single_simulation_summary = mh.summarise_game_simulation(single_simulation_results)
print()
cs.print("Summary for the same simulation", style = "underline")
print(single_simulation_summary)

# Run multiple simulations and summarize each to produce a dataset
multi_simulation_df = mh.iterate_monty_hall(50, 5)
print()
cs.print("Summary for multiple simulations", style = "underline")
print(multi_simulation_df)
print()
