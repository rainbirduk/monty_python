import monty_hall_functions as mh

print("")
print("Make your own Monty Hall Simulation and test the strategy for yourself")
print("")

n_simulations = int(input("How many simulations of Monty Hally would you like to perform? "))
n_rounds = int(input("And how many rounds would you like to play per simulation? "))

simulation_results = mh.iterate_monty_hall(n_rounds, n_simulations)

print(simulation_results.head())

# produce a bunch of summerary statistics, t.test, graphs etc. 


