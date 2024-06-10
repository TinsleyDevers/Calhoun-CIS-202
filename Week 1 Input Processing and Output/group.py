# 2 groups eats a different number of slices (2 inputs

pizzaslices = 8

group1 = int(input("How many slices does group 1 eat?: "))
group2 = int(input("How many slices does group 2 eat?: "))

slicetotal = group1 + group2
pizzatotal = slicetotal // pizzaslices
leftovers = slicetotal % pizzaslices

if leftovers > 0:
    pizzatotal += 1
    leftovers = pizzaslices - leftovers

print(f"You need {pizzatotal} pizzas.")
print(f"There will be {leftovers} leftover slices.")
