import monty_hall_functions as mh
import print_and_input_functions as tx

# introduction
tx.print_intro()

# winning box
winning_box = mh.allocate_winning_box()

# make a dict to express numbers as words
tx.box_text_dict

# # contestant chooses a box
initial_choice = tx.input_initial_choice()

# host gives a hint that is not winning_box or initial_choice
host_hint = mh.host_gives_a_hint(winning_box, initial_choice)
tx.print_host_hint(host_hint)

# contestant chooses tactic and confirms a tactic
final_choice = tx.input_choose_and_confirm_tactic(initial_choice, host_hint)

# reveal the game outcome
tx.print_game_outcome(final_choice, winning_box)





