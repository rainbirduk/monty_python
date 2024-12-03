import subprocess as sb
from rich.console import Console
cs = Console()

cs.print("The Monty Hall game rules and assumptions", style = "underline")

print("")
cs.print("Game outline", style = "underline")
print("You are on a game show and the host presents you with three boxes.")
print("Inside one box are the keys to a new sports bike; the other two boxes are empty.")

print("")
print("The game runs like this:")
print("1. The contestant first chooses a box but does not open it")
print("2. The host gives a hint that is niether the winning box nor the initial_choice")
print("3. The contestant decides whether or not to switch their choice to the remaining box")
print("4. Their final choice box is opened to reveal the outcome of the game")

print("")
print("Standard assumptions:")
print("- The prize is equally likely to be behind any door.")
print("- The host will always open a box that the contestant did not choose.")
print("- The host will always reveal an empty box and never the car the prize.")
print("- If the contestant's first choice is the prize, the host will always reveal from the remaining boxes at random.")


