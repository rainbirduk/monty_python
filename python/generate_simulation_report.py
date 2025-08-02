import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.backends.backend_pdf import PdfPages
import webbrowser as wb
import os
import print_and_input_functions as tx


def generate_simulation_report(simulation_results, summary_table, 
                               n_simulations, n_games, tactic_allocation, 
                               user_name, simulation_date):
    """
    Generates and saves a PDF report summarizing the results of a Monty Hall simulation.

    The report includes:
        - A timestamped title and formatted simulation date
        - A boxplot of success rates by tactic
        - A summary statistics table for each tactic
        - A text block describing simulation parameters
        - A footer with attribution and a GitHub link

    The PDF is saved to an 'outputs' subdirectory in the parent folder of the current working directory.
    If the directory does not exist, it is created automatically.

    Args:
        simulation_results (DataFrame): Detailed results from the simulation runs.
        summary_table (DataFrame): Summary statistics (e.g., mean, std) grouped by tactic.
        n_simulations (int): Number of simulations performed.
        n_games (int): Number of games per simulation.
        tactic_allocation (str): Strategy used to allocate tactics ('random', 'fixed', etc.).
        user_name (str): Optional user name for personalizing the report title.
        simulation_date (datetime): Timestamp of when the simulation was run.

    Returns:
        None. Opens the generated PDF in the default viewer and prints the filename.
    """
    # Format timestamp and extract year for report metadata
    timestamp = simulation_date.strftime("%Y-%m-%d_%H-%M-%S")
    year = simulation_date.year

    # Define output directory and construct full file path for the PDF
    current_directory = os.getcwd()
    parent_directory = os.path.dirname(current_directory)
    outputs_subdir = 'outputs'
    outputs_fullpath = os.path.join(parent_directory, outputs_subdir)
    if not os.path.exists(outputs_fullpath):
        os.makedirs(outputs_fullpath)
    pdf_filename = f'Monty_Hall_simulation_{timestamp}_report.pdf'
    pdf_fullpath = os.path.join(outputs_fullpath, pdf_filename)

    # Initialize PDF layout with custom grid specification
    fig = plt.figure(figsize=(7, 6))  
    gs = gridspec.GridSpec(4, 1, height_ratios=[0.05, 5, 0.7, 0.2])

    # Add title and formatted date to the top of the report
    formatted_time = f"{simulation_date.strftime('%A,')} {tx.ordinal(simulation_date.day)} {simulation_date.strftime('%B %Y at %I:%M %p')}"
    title = f"{user_name}Monty Hall game simulation"
    fig.text(0.5, 0.95, title, ha="center", va="top", fontsize=16, weight="bold")
    fig.text(0.5, 0.9, formatted_time, ha="center", va="top", fontsize=12)

    # Create boxplot of success rates grouped by tactic
    ax_plot = fig.add_subplot(gs[1])
    simulation_results.boxplot(column='success_rate', by='tactic', ax=ax_plot, grid=False)
    ax_plot.get_figure().suptitle('')
    ax_plot.set_title("", fontsize=1)
    ax_plot.set_ylabel('Success rate')
    ax_plot.set_xlabel('')

    # Display summary statistics table below the plot
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

    # Add descriptive text block with simulation parameters
    ax_text = fig.add_subplot(gs[3])
    ax_text.axis("off")
    ax_text.text(0, 1, f"Results from {n_simulations} simulations with {n_games} games per simulation", fontsize=10)
    ax_text.text(0, -1, f"Game tactics allocated {tactic_allocation}ly", fontsize=10)

    # Append footer with attribution and GitHub repository link
    pre_text = f"\u00A9 {year} Robert Funabashi:"
    link_text = "rainbirduk/monty_python"
    ax_text.text(0, -5, pre_text, fontsize=8)
    link_obj = ax_text.text(0.27, -5, link_text, fontsize=8, ha='left', color='blue')
    link_obj.set_url("https://github.com/rainbirduk/monty_python")

    # Adjust vertical spacing between layout elements
    plt.subplots_adjust(hspace=0.5)  

    # Save the figure to PDF and close the plot
    with PdfPages(pdf_fullpath) as pdf:
        pdf.savefig(fig)
        plt.close()
    
    # Open the generated PDF in the default system viewer
    wb.open_new(f"file://{pdf_fullpath}")
    print("")
    print(f"PDF saved as {pdf_filename}")

