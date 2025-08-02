import re
from datetime import datetime

import monty_hall_functions as mh
import print_and_input_functions as tx
import generate_simulation_report as sim_rpt

print("")
print("Make your own Monty Hall Simulation and test the strategy for yourself")

# Prompt user for a name (optional) and format it for display
print("")
user_name = input("What is your name? (optional, hit enter to skip) ")
if user_name != "":
    user_name = re.sub(r"s's", "s'", user_name + "'s ").capitalize()

# Collect simulation parameters from user input
n_simulations = tx.choose_n_simulations()
n_games = tx.choose_n_games()
tactic_allocation = tx.allocate_tactic()

# Record the current date and time for timestamping the report
simulation_date = datetime.now()

# Run the Monty Hall simulation using the specified parameters
simulation_results = mh.iterate_monty_hall(n_games, n_simulations, tactic_allocation)

# Compute summary statistics for each tactic used in the simulation
summary_table = simulation_results.groupby('tactic')['success_rate'].describe().round(2)
summary_table.index.name = None

# Generate a PDF report containing results, summary statistics, and metadata
sim_rpt.generate_simulation_report(simulation_results, summary_table, 
                                   n_simulations, n_games, tactic_allocation, 
                                   user_name, simulation_date)
