import monty_hall_functions as mh
import print_and_input_functions as tx

# Display introductory text explaining the Monty Hall game
tx.print_intro()

# Randomly assign the winning door for this round
winning_door = mh.allocate_winning_door()

# Prompt the contestant to choose an initial door
initial_choice = tx.input_initial_choice()

# Host reveals a non-winning, non-chosen door as a hint
host_hint = mh.host_gives_a_hint(winning_door, initial_choice)
tx.print_host_hint(host_hint)

# Contestant selects and confirms a tactic (switch or stay), then finalizes their choice
final_choice = tx.input_choose_and_confirm_tactic(initial_choice, host_hint)

# Reveal whether the contestant won or lost based on their final choice
tx.print_game_outcome(final_choice, winning_door)
