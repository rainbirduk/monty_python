import monty_hall_functions as mh
import pandas as pd
import re
import matplotlib.pyplot as plt
from IPython.display import HTML, display
import webbrowser
import os


print("")
print("Make your own Monty Hall Simulation and test the strategy for yourself")
print("")

# set file paths
current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

png_filepath = 'outputs/box_plot.png'
png_filepath = os.path.join(parent_directory, png_filepath)

html_filepath = 'outputs/monty_hall_report.html'
html_filepath = os.path.join(parent_directory, html_filepath)

# set the user name
user_name = input("What is your name? ").capitalize()

# set the number of simulations and game rounds   
n_simulations = int(input(f"How many simulations of Monty Hall would you like to perform, {user_name}? "))
n_rounds = int(input("And how many rounds would you like to play per simulation? "))

# simulate the game
simulation_results = mh.iterate_monty_hall(n_rounds, n_simulations)

# Display the plot
plt.show()

# Generate summary statistics table
summary_table = simulation_results.groupby('tactic')['success_rate'].describe().reset_index()

# Generate a box plot
plt.figure(figsize=(10, 6))
simulation_results.boxplot(column='success_rate', by='tactic', grid=False)
plt.title('Monty Hall tactics')
plt.suptitle('')  # Suppress the default title to avoid duplication
plt.xlabel('Tactic')
plt.ylabel('Success rate')
plt.savefig(png_filepath)  # Save the plot as a PNG file
plt.close()

# clean the username 
user_name = re.sub(r"s's", "s'", user_name + "'s")

# Create summary text
summary_text = f"""
<h1>{user_name} Monty Hall Simulation </h1>
<p>This report contains the results of a simulation comparing the success rates of two tactics: "switch" and "stick".</p>
"""

# Create the HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Monty Hall Simulation Report</title>
</head>
<body>
    {summary_text}
    <h2>Box Plot</h2>
    <img src="box_plot.png" alt="Box Plot">
    <h2>Summary Statistics</h2>
    {summary_table.to_html(index=False)}
</body>
</html>
"""

# Save the HTML report to a file
with open(html_filepath, 'w') as f:
    f.write(html_content)

# print save location    
print("")
print("Your simulation report is saved to", html_filepath)

# Open the saved HTML file in the default web browser 
webbrowser.open(html_filepath)
