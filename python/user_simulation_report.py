import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import gridspec
import re
import os
from datetime import datetime
import monty_hall_functions as mh
import matplotlib.pyplot as plt
import print_and_input_functions as tx
import webbrowser as wb
import print_and_input_functions as tx


print("")
print("Make your own Monty Hall Simulation and test the strategy for yourself")

# get date information
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
year = now.year

# set file paths
current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
pdf_local_path = f'outputs\Monty_Hall_simulation_report_{timestamp}.pdf'
pdf_fullpath = os.path.join(parent_directory, pdf_local_path)

# set the username
user_name = input("What is your name? (optional, hit enter to skip) ")
if user_name != "":
    user_name = re.sub(r"s's", "s'", user_name + "'s ").capitalize()

# choose simulation parameters
n_simulations = tx.choose_n_simulations()
n_rounds = tx.choose_n_rounds()
tactic_allocation = tx.allocate_tactic()

# simulate the game
simulation_results = mh.iterate_monty_hall(n_rounds, n_simulations, tactic_allocation)

# generate summary statistics table
summary_table = simulation_results.groupby('tactic')['success_rate'].describe().round(2)
summary_table.index.name = None

# set up the report template
fig = plt.figure(figsize=(7, 6))  
gs = gridspec.GridSpec(4, 1, height_ratios=[0.05, 5, 0.7, 0.2])  # [title, plot, table, text]

# build formatted date string
formatted_time = f"{now.strftime('%A,')} {tx.ordinal(now.day)} {now.strftime('%B %Y at %I:%M %p')}"

# generate the title and date
title = f"{user_name}Monty Hall game simulation"
fig.text(0.5, 0.95, title, ha="center", va="top", fontsize=16, weight="bold")
fig.text(0.5, 0.9, formatted_time, ha="center", va="top", fontsize=12)

# boxplot
ax_plot = fig.add_subplot(gs[1])
simulation_results.boxplot(column='success_rate', by='tactic', ax=ax_plot, grid=False)
ax_plot.get_figure().suptitle('')
ax_plot.set_title("", fontsize=1)
ax_plot.set_ylabel('Success rate')
ax_plot.set_xlabel('')

# summary stats table
ax_table = fig.add_subplot(gs[2])
ax_table.axis("off")
table = ax_table.table(
    cellText=summary_table.values,
    colLabels=summary_table.columns,
    rowLabels=summary_table.index,
    loc="upper left",
    cellLoc="center"
)
table.scale(1.0, 1.2)

# report the inputs as text
ax_text = fig.add_subplot(gs[3])
ax_text.axis("off")
ax_text.text(0, 1, f"Results from {n_simulations} simulations with {n_rounds} games per simulation", fontsize=10)
ax_text.text(0, -1, f"Game tactics allocated {tactic_allocation}ly", fontsize=10)

# create a footer
pre_text = f"\u00A9 {year} Robert Funabashi:"
link_text = "rainbirduk/monty_python"
ax_text.text(0, -5, pre_text, fontsize=8)
link_obj = ax_text.text(0.27, -5, link_text, fontsize=8, ha='left', color='blue')
link_obj.set_url("https://github.com/rainbirduk/monty_python")

# increase vertical space between subplots
plt.subplots_adjust(hspace=0.5)  

# save and open the PDF
with PdfPages(pdf_fullpath) as pdf:
    pdf.savefig(fig)
    plt.close()
wb.open_new(f"file://{pdf_fullpath}")

# feedback to user
print("")
print(f"PDF saved to {pdf_local_path}")

