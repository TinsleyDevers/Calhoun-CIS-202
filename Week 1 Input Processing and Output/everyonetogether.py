# Total number of slices to be eaten (1 input)

pizzaslices = 8
family = 4

slices_per = int(input("How many slices will everyone eat?: "))

neededslices = slices_per * family

pizzatotal = neededslices // pizzaslices
leftovers = neededslices % pizzaslices

if leftovers > 0:
    pizzatotal += 1
    leftovers = pizzaslices - leftovers

print(f"You need {pizzatotal} pizzas.")
print(f"There will be {leftovers} leftover slices.")
