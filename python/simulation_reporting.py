import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import gridspec
import webbrowser as wb
import print_and_input_functions as tx

def extract_timestamp(simulation_date):
    """
    Extracts a formatted timestamp and year from the simulation date.

    Args:
        simulation_date (datetime): The date and time of the simulation.

    Returns:
        tuple[str, int]: A timestamp string and the corresponding year.
    """
    timestamp = simulation_date.strftime("%Y-%m-%d_%H-%M-%S")
    year = simulation_date.year
    return timestamp, year

def prepare_output_path(timestamp):
    """
    Constructs the full file path for saving the PDF report.

    Creates the 'outputs' directory in the parent folder if it doesn't exist.

    Args:
        timestamp (str): Timestamp to include in the filename.

    Returns:
        str: Full path to the PDF file.
    """
    current_directory = os.getcwd()
    parent_directory = os.path.dirname(current_directory)
    outputs_subdir = 'outputs'
    outputs_fullpath = os.path.join(parent_directory, outputs_subdir)
    if not os.path.exists(outputs_fullpath):
        os.makedirs(outputs_fullpath)
    pdf_filename = f'Monty_Hall_simulation_{timestamp}_report.pdf'
    return os.path.join(outputs_fullpath, pdf_filename)

def setup_pdf_layout():
    """
    Initializes the PDF figure and grid layout.

    Returns:
        tuple[Figure, GridSpec]: The matplotlib figure and grid specification.
    """
    fig = plt.figure(figsize=(7, 6))  
    gs = gridspec.GridSpec(4, 1, height_ratios=[0.05, 5, 0.7, 0.2])
    return fig, gs

def add_title_and_date(fig, simulation_date, user_name):
    """
    Adds the title and formatted date to the top of the PDF report.

    Args:
        fig (Figure): The matplotlib figure.
        simulation_date (datetime): The date of the simulation.
        user_name (str): Optional user name for personalization.
    """
    formatted_time = f"{simulation_date.strftime('%A,')} {tx.ordinal(simulation_date.day)} {simulation_date.strftime('%B %Y at %I:%M %p')}"
    title = f"{user_name}Monty Hall game simulation"
    fig.text(0.5, 0.95, title, ha="center", va="top", fontsize=16, weight="bold")
    fig.text(0.5, 0.9, formatted_time, ha="center", va="top", fontsize=12)

def add_boxplot(fig, ax_slot, simulation_results):
    """
    Adds a boxplot of success rates by tactic to the report.

    Args:
        fig (Figure): The matplotlib figure.
        ax_slot (SubplotSpec): Grid slot for the plot.
        simulation_results (DataFrame): Simulation results with success rates.
    """
    ax_plot = fig.add_subplot(ax_slot)
    simulation_results.boxplot(column='success_rate', by='tactic', ax=ax_plot, grid=False)
    ax_plot.get_figure().suptitle('')
    ax_plot.set_title("", fontsize=1)
    ax_plot.set_ylabel('Success rate')
    ax_plot.set_xlabel('')

def add_summary_table(fig, ax_slot, summary_table):
    """
    Adds a summary statistics table to the report.

    Args:
        fig (Figure): The matplotlib figure.
        ax_slot (SubplotSpec): Grid slot for the table.
        summary_table (DataFrame): Summary statistics grouped by tactic.
    """
    ax_table = fig.add_subplot(ax_slot)
    ax_table.axis("off")
    table = ax_table.table(
        cellText=summary_table.values,
        colLabels=summary_table.columns,
        rowLabels=summary_table.index,
        loc="upper left",
        cellLoc="center"
    )
    table.scale(1.0, 1.2)

def add_simulation_text(fig, ax_slot, n_simulations, n_games, tactic_allocation):
    """
    Adds descriptive text about the simulation parameters.

    Args:
        fig (Figure): The matplotlib figure.
        ax_slot (SubplotSpec): Grid slot for the text block.
        n_simulations (int): Number of simulations run.
        n_games (int): Number of games per simulation.
        tactic_allocation (str): Tactic assignment method.
    """
    ax_text = fig.add_subplot(ax_slot)
    ax_text.axis("off")
    ax_text.text(0, 1, f"Results from {n_simulations} simulations with {n_games} games per simulation", fontsize=10)
    ax_text.text(0, -1, f"Game tactics allocated {tactic_allocation}ly", fontsize=10)

def add_footer(fig, ax_slot, year):
    """
    Adds a footer with attribution and a GitHub link.

    Args:
        fig (Figure): The matplotlib figure.
        ax_slot (SubplotSpec): Grid slot for the footer.
        year (int): Year of the simulation.
    """
    ax_text = fig.add_subplot(ax_slot)
    ax_text.axis("off")
    pre_text = f"\u00A9 {year} Robert Funabashi:"
    link_text = "rainbirduk/monty_python"
    ax_text.text(0, -5, pre_text, fontsize=8)
    link_obj = ax_text.text(0.27, -5, link_text, fontsize=8, ha='left', color='blue')
    link_obj.set_url("https://github.com/rainbirduk/monty_python")

def save_and_open_pdf(fig, pdf_fullpath):
    """
    Saves the figure as a PDF and opens it in the default viewer.

    Args:
        fig (Figure): The matplotlib figure.
        pdf_fullpath (str): Full path to save the PDF file.
    """
    plt.subplots_adjust(hspace=0.5)
    with PdfPages(pdf_fullpath) as pdf:
        pdf.savefig(fig)
        plt.close()
    wb.open_new(f"file://{pdf_fullpath}")
    print("")
    print(f"PDF saved as {os.path.basename(pdf_fullpath)}")

def generate_simulation_report(simulation_results, summary_table, 
                               n_simulations, n_games, tactic_allocation, 
                               user_name, simulation_date):
    """
    Orchestrates the creation of a PDF report summarizing Monty Hall simulation results.

    Args:
        simulation_results (DataFrame): Detailed results from the simulation runs.
        summary_table (DataFrame): Summary statistics grouped by tactic.
        n_simulations (int): Number of simulations performed.
        n_games (int): Number of games per simulation.
        tactic_allocation (str): Strategy used to allocate tactics.
        user_name (str): Optional user name for personalizing the report.
        simulation_date (datetime): Timestamp of when the simulation was run.
    """
    timestamp, year = extract_timestamp(simulation_date)
    pdf_fullpath = prepare_output_path(timestamp)
    fig, gs = setup_pdf_layout()

    add_title_and_date(fig, simulation_date, user_name)
    add_boxplot(fig, gs[1], simulation_results)
    add_summary_table(fig, gs[2], summary_table)
    add_simulation_text(fig, gs[3], n_simulations, n_games, tactic_allocation)
    add_footer(fig, gs[3], year)

    save_and_open_pdf(fig, pdf_fullpath)
