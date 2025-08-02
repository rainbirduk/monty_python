import pandas as pd
import random as rd
import subprocess as sb


######################
### Game variables ###

# Tuple of door numbers used in the Monty Hall game
doors = (1, 2, 3)

# Tuple of player tactics: either switching or sticking with the initial choice
tactics = ("switch", "stick")

# Mapping of boolean game outcomes to result labels
results = {True: "Win", False: "Lose"}


######################
### Game functions ###

def allocate_winning_door() -> int:
    """
    Randomly selects one of the doors to be the winning door.

    Returns:
        int: The number of the winning door.
    """
    return rd.choice(doors) 

def choose_initial_door(door_choice=rd.choice(doors)) -> int:
    """
    Validates the player's initial door choice.

    If the provided choice is not one of the available doors, the user is prompted
    to enter a valid door number until a correct input is given.

    Args:
        door_choice (int, optional): The initial door selection. Defaults to a random door.

    Returns:
        int: A valid door number from the available options.
    """
    door_choice = int(door_choice)
    while door_choice not in doors:
        print("")
        print("Sorry, but", door_choice, "is not a valid guess.")
        door_choice = int(input("Enter a door number between 1 an 3: "))
    return door_choice

def host_gives_a_hint(winning_door: int, initial_choice: int) -> int:
    """
    Simulates the host revealing a non-winning, non-chosen door.

    Args:
        winning_door (int): The door with the prize.
        initial_choice (int): The player's initial door selection.

    Returns:
        int: A door number that is neither the winning door nor the player's choice.
    """
    host_choices = [door for door in doors if door not in 
                    [winning_door, initial_choice]]
    return rd.choice(host_choices) 

def choose_tactic(initial_choice: int, host_hint: int, tactic: str) -> int:
    """
    Determines the contestant's final door choice based on their tactic.

    If the tactic is 'switch', the final choice is the remaining unopened door.
    If the tactic is 'stick', the final choice remains the initial selection.

    Args:
        initial_choice (int): The player's initial door selection.
        host_hint (int): The door revealed by the host.
        tactic (str): The player's strategy, either 'switch' or 'stick'.

    Returns:
        int: The contestant's final door choice.
    """
    if tactic == "switch":
        final_choice = [door for door in doors if door not in 
                        [host_hint, initial_choice]][0]
    else:
        final_choice = initial_choice
    return final_choice

def assign_outcome(final_choice: int, winning_door: int) -> bool:
    """
    Determines whether the contestant's final choice is the winning door.

    Args:
        final_choice (int): The door selected by the contestant.
        winning_door (int): The door with the prize.

    Returns:
        bool: True if the final choice matches the winning door, False otherwise.
    """
    return final_choice == winning_door


############################
### Simulation functions ###

def play_monty_hall(tactic: str = rd.choice(tactics)) -> dict[str, str]:
    """
    Simulates a single Monty Hall game using the specified tactic.

    The game proceeds through random door allocation, initial choice,
    host hint, tactic application, and outcome determination.

    Args:
        tactic (str, optional): The player's strategy, either 'switch' or 'stick'.
                                Defaults to a random tactic.

    Returns:
        dict[str, str]: A dictionary containing the tactic used and the result ('Win' or 'Lose').
    """
    winning_door = allocate_winning_door()
    initial_choice = choose_initial_door()
    host_hint = host_gives_a_hint(winning_door, initial_choice)
    final_choice = choose_tactic(initial_choice, host_hint, tactic)
    outcome = assign_outcome(final_choice, winning_door)
    return {"tactic" : tactic, "result" : results[outcome]}

def simulate_monty_hall(n_rounds: int = 5, tactic: str = rd.choice(tactics)) -> pd.DataFrame:
    """
    Simulates multiple rounds of the Monty Hall game using a single tactic.

    Each round is played automatically, and the results are collected into a DataFrame.

    Args:
        n_rounds (int, optional): Number of game rounds to simulate. Defaults to 5.
        tactic (str, optional): The tactic used in all rounds ('switch' or 'stick').
                                Defaults to a random tactic.

    Returns:
        pd.DataFrame: A DataFrame containing the tactic and result for each round.
    """
    dict_list = []
    for round in range(n_rounds):
        result = play_monty_hall(tactic) 
        dict_list.append(result)
    df = pd.DataFrame(dict_list)
    return df
 
def summarise_game_simulation(simulation_results: pd.DataFrame) -> dict[str, float]:
    """
    Calculates the win rate from a Monty Hall simulation using a single tactic.

    Args:
        simulation_results (pd.DataFrame): A DataFrame containing 'tactic' and 'result' columns
                                           for each simulated round.

    Returns:
        dict[str, float]: A dictionary with the tactic used and its corresponding success rate.
    """
    tactic = simulation_results["tactic"][0]
    total_wins = simulation_results[simulation_results['result'] == 'Win'].shape[0]
    total_rounds = simulation_results.shape[0]
    win_rate = total_wins / total_rounds
    summary_dict = {"tactic" : tactic, "success_rate" : win_rate}
    return summary_dict

def iterate_monty_hall(n_rounds: int, n_simulations: int, tactic_allocation: str = "random") -> pd.DataFrame:
    """
    Runs multiple Monty Hall simulations and summarizes win rates for each.

    For each simulation, a tactic is selected based on the allocation method:
    either randomly or alternating equally between 'switch' and 'stick'.

    Args:
        n_rounds (int): Number of rounds per simulation.
        n_simulations (int): Number of simulations to run.
        tactic_allocation (str, optional): Method for assigning tactics ('random' or 'equal').
                                           Defaults to 'random'.

    Returns:
        pd.DataFrame: A DataFrame summarizing the tactic and success rate for each simulation.
    """
    dict_list = []
    tactic_pendulum = rd.choice([1,2])
    for sim in range(n_simulations):
        if tactic_allocation == "random":
            tactic = rd.choice(tactics)
        elif tactic_allocation == "equal":
            tactic = tactics[tactic_pendulum % 2]
            tactic_pendulum = tactic_pendulum + 1
        simulation_results = simulate_monty_hall(n_rounds, tactic) 
        simulation_summary = summarise_game_simulation(simulation_results)
        dict_list.append(simulation_summary)
    df = pd.DataFrame(dict_list)
    return df


###############
### Testing ###

# Run the test script for Monty Hall functions when this file is executed directly
if __name__ == "__main__":
    sb.run(['python', 'monty_hall_functions_test.py'])
