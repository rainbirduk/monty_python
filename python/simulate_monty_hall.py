import monty_hall_functions as mh
import pandas as pd
import re
import matplotlib.pyplot as plt
import os
import print_and_input_functions as tx
import webbrowser as wb
from pathlib import Path


print("")
print("Make your own Monty Hall Simulation and test the strategy for yourself")
print("")

# set file paths
current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

png_filepath = 'outputs/box_plot.pdf'
png_filepath = os.path.join(parent_directory, png_filepath)

# set the parameters with user input 
#user_name = input("What is your name? ")
user_name = 'Robert'
user_name = re.sub(r"s's", "s'", user_name + "'s").capitalize()

# n_simulations = tx.choose_n_simulations()
# n_rounds = tx.choose_n_rounds()
# tactic_allocation = tx.allocate_tactic()

n_simulations = 100
n_rounds = 20
tactic_allocation = 'random'

# simulate the game
simulation_results = mh.iterate_monty_hall(n_rounds, n_simulations, tactic_allocation)
print(simulation_results)


# Generate summary statistics table
summary_table = simulation_results.groupby('tactic')['success_rate'].describe().round(2)
summary_table.index.name = None
print(summary_table)
print(type(summary_table))


# # Generate a box plot
# plt.figure(figsize=(10, 6))
# simulation_results.boxplot(column='success_rate', by='tactic', grid=False)
# plt.title("Success rate in Monty Hall for 'stick' and 'switch' tactics")
# plt.suptitle('')  # suppress the default title to avoid duplication
# plt.xlabel('Tactic')
# plt.ylabel('Success rate')

# # # Display the plot
# # plt.show()

# # # Save the plot as a PNG file
# plt.savefig(png_filepath, format='pdf')  
# plt.close()

# # convert filepath to URI and open
# uri = Path(png_filepath).resolve().as_uri()
# wb.open_new(uri)


