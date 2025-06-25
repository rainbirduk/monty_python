import re
from datetime import datetime

import monty_hall_functions as mh
import print_and_input_functions as tx
import generate_simulation_report as sim_rpt

print("")
print("Make your own Monty Hall Simulation and test the strategy for yourself")

# set the username
print("")
user_name = input("What is your name? (optional, hit enter to skip) ")
if user_name != "":
    user_name = re.sub(r"s's", "s'", user_name + "'s ").capitalize()

# choose simulation parameters
n_simulations = tx.choose_n_simulations()
n_games = tx.choose_n_games()
tactic_allocation = tx.allocate_tactic()

# get the date and time of the simulation
simulation_date = datetime.now()

# simulate the game
simulation_results = mh.iterate_monty_hall(n_games, n_simulations, tactic_allocation)

# generate summary statistics table
summary_table = simulation_results.groupby('tactic')['success_rate'].describe().round(2)
summary_table.index.name = None

# generate the pdf report
sim_rpt.generate_simulation_report(simulation_results, summary_table, 
                                   n_simulations, n_games, tactic_allocation, 
                                   user_name, simulation_date)

