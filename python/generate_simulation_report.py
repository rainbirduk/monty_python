import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.backends.backend_pdf import PdfPages
import webbrowser as wb
import os
import print_and_input_functions as tx


def generate_simulation_report(simulation_results, summary_table, 
                               n_simulations, n_games, tactic_allocation, 
                               user_name, simulation_date):

    # get date information
    timestamp = simulation_date.strftime("%Y-%m-%d_%H-%M-%S")
    year = simulation_date.year

    # set file paths
    current_directory = os.getcwd()
    parent_directory = os.path.dirname(current_directory)
    outputs_subdir = 'outputs'
    pdf_filename = f'Monty_Hall_simulation_{timestamp}_report.pdf'
    pdf_fullpath = os.path.join(parent_directory, outputs_subdir, pdf_filename)

    # set up the PDF layout
    fig = plt.figure(figsize=(7, 6))  
    gs = gridspec.GridSpec(4, 1, height_ratios=[0.05, 5, 0.7, 0.2])

    # format the date and title
    formatted_time = f"{simulation_date.strftime('%A,')} {tx.ordinal(simulation_date.day)} {simulation_date.strftime('%B %Y at %I:%M %p')}"
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

    # text block for input info
    ax_text = fig.add_subplot(gs[3])
    ax_text.axis("off")
    ax_text.text(0, 1, f"Results from {n_simulations} simulations with {n_games} games per simulation", fontsize=10)
    ax_text.text(0, -1, f"Game tactics allocated {tactic_allocation}ly", fontsize=10)

    # footer and github link
    pre_text = f"\u00A9 {year} Robert Funabashi:"
    link_text = "rainbirduk/monty_python"
    ax_text.text(0, -5, pre_text, fontsize=8)
    link_obj = ax_text.text(0.27, -5, link_text, fontsize=8, ha='left', color='blue')
    link_obj.set_url("https://github.com/rainbirduk/monty_python")

    # Spacing
    plt.subplots_adjust(hspace=0.5)  

    # Save PDF
    with PdfPages(pdf_fullpath) as pdf:
        pdf.savefig(fig)
        plt.close()
    
    wb.open_new(f"file://{pdf_fullpath}")
    print("")
    print(f"PDF saved as {pdf_filename}")
